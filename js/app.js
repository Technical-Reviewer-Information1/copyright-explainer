(function () {
  'use strict';
  const $ = id => document.getElementById(id);
  const NOW = 2026;

  /* ===== STEP 1 ===== */
  function drawTL() {
    const d = +$('deathY').value || 0, end = d + 70;
    const min = Math.min(d, 1700), max = Math.max(end, NOW) + 10;
    const pos = y => (y - min) / (max - min) * 100;
    $('tlBox').innerHTML =
      '<i style="left:' + pos(d) + '%;width:' + Math.max(0, pos(end) - pos(d)) + '%"></i>' +
      '<span class="now" style="left:' + pos(NOW) + '%"></span>' +
      '<span class="lb" style="left:' + pos(d) + '%">没' + d + '</span>' +
      '<span class="lb" style="left:' + Math.min(88, pos(end)) + '%">' + end + '年まで</span>';
    const over = NOW > end;
    const n = $('tlNote');
    n.className = 'note ' + (over ? 'ok' : 'warn');
    n.innerHTML = d + '年に亡くなった著作者の作品は、<strong>' + end + '年の年末まで</strong>保護されます。<br>' +
      (over
        ? '現在（' + NOW + '年）はすでに保護期間が終わっており、<strong>パブリックドメイン</strong>です。自分で演奏して投稿しても、作曲者の権利の侵害にはなりません。'
        : 'まだ保護期間中です（あと約 ' + (end - NOW) + ' 年）。利用には許諾が必要です。');
  }

  /* ===== STEP 2 ===== */
  const RULES = [
    { t: '自作部分が主、引用部分が従になっている', w: '引用が大部分を占めるものは引用とは認められません。' },
    { t: '引用する必然性がある', w: 'なくても成り立つ引用は認められません。' },
    { t: '引用部分が本文と区別できる（かぎかっこ・書式など）', w: 'どこからが引用か分かるようにします。' },
    { t: '引用部分を改変していない', w: '<strong>数行アレンジするのも改変にあたります。</strong>' },
    { t: '出典・出所を明記している', w: '書名・著者名・掲載ページなどを示します。' }
  ];
  function drawRules() {
    $('ruleBox').innerHTML = RULES.map((r, i) =>
      '<label><input type="checkbox" data-i="' + i + '"><span>' + r.t + '<br><span class="small" style="color:var(--muted)">' + r.w + '</span></span></label>').join('');
    $('ruleBox').querySelectorAll('input').forEach(x => x.addEventListener('change', () => {
      const n = $('ruleBox').querySelectorAll('input:checked').length;
      const nt = $('ruleNote');
      nt.className = 'note ' + (n === RULES.length ? 'ok' : 'info');
      nt.innerHTML = n + ' / ' + RULES.length + ' 条件' +
        (n === RULES.length ? '<br>すべて満たしていれば、<strong>著作権者の許諾がなくても引用できます</strong>。1つでも欠けると著作権侵害になるおそれがあります。' : '');
    }));
    $('ruleNote').className = 'note info';
    $('ruleNote').textContent = '0 / ' + RULES.length + ' 条件';
  }

  /* ===== STEP 3 ===== */
  const CCOPT = [
    { id: 'BY', t: 'BY', d: '作品のクレジット（作者名など）を表示すること', must: true },
    { id: 'NC', t: 'NC', d: '営利目的で利用しないこと' },
    { id: 'ND', t: 'ND', d: '元の作品を改変しないこと' },
    { id: 'SA', t: 'SA', d: '（改変してよいが）元の作品のライセンスを継承すること' }
  ];
  let cc = { BY: true, NC: false, ND: false, SA: false };
  function drawCC() {
    $('ccOpts').innerHTML = CCOPT.map(o =>
      '<label' + (o.must ? ' class="dis"' : '') + '><input type="checkbox" data-id="' + o.id + '"' +
      (cc[o.id] ? ' checked' : '') + (o.must ? ' disabled' : '') + '>' +
      '<span><span class="t">' + o.t + '</span>' + (o.must ? '（必須）' : '') + '<br><span class="d">' + o.d + '</span></span></label>').join('');
    $('ccOpts').querySelectorAll('input:not([disabled])').forEach(x => x.addEventListener('change', () => {
      cc[x.dataset.id] = x.checked; drawCC();
    }));
    const parts = CCOPT.filter(o => cc[o.id]).map(o => o.t);
    $('ccOut').innerHTML = '<span class="ccbadge"><span class="cc">CC</span>' + parts.join(' ') + '</span>';
    const n = $('ccNote');
    if (cc.ND && cc.SA) {
      n.className = 'note ng';
      n.innerHTML = '<strong>この組合せは指定できません。</strong>ND は「改変してはいけない」、SA は「改変したときは同じライセンスを継承する」という意味なので、<strong>矛盾します</strong>。';
    } else {
      n.className = 'note ok';
      n.innerHTML = '有効な組合せです。' +
        (cc.NC ? '営利目的では使えません。' : '営利目的でも使えます。') +
        (cc.ND ? '改変はできません。' : (cc.SA ? '改変できますが、同じライセンスで公開する必要があります。' : '改変も自由です。'));
    }
  }
  const BANK = [
    { no: '⓪', p: ['BY'], bad: false, why: 'BYのみ。最も自由に使えるライセンスです。' },
    { no: '①', p: ['BY', 'ND', 'SA'], bad: true, why: '<strong>NDとSAは矛盾</strong>します。改変を禁止しながら、改変時のライセンス継承を求めることはできません。' },
    { no: '②', p: ['BY', 'NC', 'SA'], bad: false, why: '非営利で、改変したら同じライセンスを継承。有効な組合せです。' },
    { no: '③', p: ['BY', 'NC', 'ND'], bad: false, why: '非営利で改変禁止。有効な組合せです。' },
    { no: '④', p: ['BY', 'ND'], bad: false, why: '改変禁止。有効な組合せです。' },
    { no: '⑤', p: ['NC', 'ND'], bad: true, why: '<strong>BYがありません</strong>。BYは必須なので、この組合せは指定できません。' }
  ];
  let bank = {};
  function drawBank() {
    $('ccBank').innerHTML = BANK.map((b, i) => {
      let cls = '';
      if (Object.keys(bank).length) cls = b.bad ? ' correct' : (bank[i] ? ' wrong' : '');
      return '<div class="b' + cls + '" data-i="' + i + '"><div class="no">' + b.no + '</div>' +
        '<span class="ccbadge"><span class="cc">CC</span>' + b.p.join(' ') + '</span></div>';
    }).join('');
    $('ccBank').querySelectorAll('.b').forEach(el => el.addEventListener('click', () => {
      const i = +el.dataset.i;
      if (bank[i]) return;
      bank[i] = true;
      const picked = Object.keys(bank).length;
      drawBank();
      const n = $('bankNote');
      const rights = Object.keys(bank).filter(k => BANK[k].bad).length;
      n.className = 'note ' + (BANK[i].bad ? 'ok' : 'ng');
      n.innerHTML = BANK[i].no + '：' + (BANK[i].bad ? '正解。' : '<strong>これは有効な組合せです。</strong>') + BANK[i].why +
        (picked >= 2 ? '<br>誤っているのは <strong>①（BY ND SA）と⑤（NC ND）</strong> の2つ。本文の答えは【ウ】・【エ】＝<strong>①・⑤</strong>（順不同）です。' : '');
    }));
    $('bankNote').className = 'note info';
    $('bankNote').textContent = '誤っている組合せを2つ見つけてください。';
  }

  function init() {
    $('deathY').addEventListener('input', drawTL);
    document.querySelectorAll('button[data-y]').forEach(b => b.addEventListener('click', () => { $('deathY').value = b.dataset.y; drawTL(); }));
    drawTL(); drawRules(); drawCC(); drawBank();
    Quiz.choice('q1Box', 'q1Note', [
      { k: 'ア', q: '日本の著作権法に基づく判断として最も適当なものは',
        ch: ['自分が撮った有名人の写真を友達にあげると、著作者の権利を侵害する', 'バッハ（1750年没）の曲を自分で演奏した動画を動画共有サイトに投稿すると、作曲者の権利を侵害する', '他人の著作物を許可なく自分のWebページに丸ごと転載しても、著作者の権利を侵害しない', '自分で購入した複数の問題集をコピーして自分が勉強するためのオリジナル問題集を作っても、著作者の権利を侵害しない'],
        a: 3, why: '私的使用のための複製（著作権法第30条）にあたります。⓪は自分で撮った写真の著作権は自分にあります（ただし肖像権に注意）。①はバッハの曲はすでにパブリックドメイン。②は複製権・公衆送信権の侵害です。' }
    ], '本文の答えは【ア】③ です。');
    Quiz.choice('q2Box', 'q2Note', [
      { k: 'イ', q: '日本の著作権法に基づく判断として最も適当なものは',
        ch: ['出典を明示した上で、書籍の一部の内容を数行程度アレンジして引用することは著作権侵害には当たらない', '自分のSNSに、裁判所の許諾を得ずに裁判の判例を掲載しても、著作権侵害には当たらない', '他人が演奏したベートーヴェン交響曲第5番「運命」の音声データをSNSに投稿することは、著作権侵害には当たらない', '有名なアイドルの楽曲が収録された音楽CDを、パソコンですべて複製して友だちに無償で渡すことは、著作権侵害には当たらない'],
        a: 1, why: '判例は著作権の保護対象外です。⓪は<strong>アレンジ＝改変</strong>なので引用のルールに反します。②は曲は自由でも<strong>演奏者の著作隣接権</strong>を侵害します。③は私的使用の範囲（本人・家庭内）を超えています。' }
    ], '本文の答えは【イ】① です。');
    window.Terms.glossary($('glossBox'), ['著作権', '著作隣接権', 'パブリックドメイン', 'クリエイティブ・コモンズ', '知的財産権', '産業財産権']);
    Worksheet.make('wsBox', {
      name: 'copyright-explainer',
      fields: [
        { id: 'c1', label: '① つくるもの', hint: '発表資料・動画・ポスターなど。公開する範囲も。', rows: 2, ph: '例：探究発表のスライド（校内発表のみ）' },
        { id: 'c2', label: '② 使いたい他人の著作物', hint: '写真・図・文章・音楽。だれの何か。', rows: 3, ph: '例：新聞社サイトのグラフ1点、教科書の文章3行' },
        { id: 'c3', label: '③ 引用の必要性', hint: 'なぜ自分のことばに置きかえられないのか。', rows: 2, ph: '例：グラフの数値そのものを示さないと主張の根拠にならないから' },
        { id: 'c4', label: '④ 主従関係と区分', hint: '自分の文章が主になっているか。かぎかっこ等で区別しているか。', rows: 3,
          ph: '例：スライド10枚のうち引用は1枚。枠で囲み「引用」と明記' },
        { id: 'c5', label: '⑤ 出典の書き方', hint: '著者・題名・発行年・URL・参照日。', rows: 3, ph: '例：◯◯新聞「〜」2025年5月1日, https://… （2026年8月21日参照）' },
        { id: 'c6', label: '⑥ 判断', hint: '引用でよいか、許諾が必要か、使わないか。', rows: 2, ph: '例：グラフは引用として使える。音楽はSNS公開なので許諾が必要と判断し、使わない' }
      ],
      build: function (v, e) {
        return '<h4>著作物チェックシート</h4><dl>' +
          '<dt>① つくるもの</dt><dd>' + e(v.c1) + '</dd>' +
          '<dt>② 使いたい著作物</dt><dd>' + e(v.c2) + '</dd>' +
          '<dt>③ 引用の必要性</dt><dd>' + e(v.c3) + '</dd>' +
          '<dt>④ 主従関係と区分</dt><dd>' + e(v.c4) + '</dd>' +
          '<dt>⑤ 出典</dt><dd>' + e(v.c5) + '</dd>' +
          '<dt>⑥ 判断</dt><dd>' + e(v.c6) + '</dd></dl>';
      },
      note: '③〜⑤のどれかが書けないときは、引用の条件を満たしていない可能性があります。'
    });

    window.Terms.attach();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
