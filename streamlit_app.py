import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

def main():
    st.set_page_config(
        page_title="著作権",
        page_icon="🎨",
        layout="wide"
    )
    
    st.title("🎨 著作権")
    st.caption("Created by Dit-Lab.(Daiki ITO)")
    st.caption("Supported by Tomoaki ATSUMI")
    
    # Progress tracking
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 1
    
    # Navigation
    step_names = [
        "はじめに - きみの「作品」は宝物だ！💎",
        "ブログ記事を作ってみよう！",
        "画像さがし - この画像、使える？使えない？🖼️",
        "BGM選び - この曲、流せる？流せない？🎵",
        "ルールを守って「引用」しよう！📚",
        "きみの権利を知り、意思表示をしよう！",
        "最終確認！これってOK？"
    ]
    
    # Progress bar
    progress = st.session_state.current_step / len(step_names)
    st.progress(progress, f"Step {st.session_state.current_step} / {len(step_names)}")
    
    # Display current step
    if st.session_state.current_step == 1:
        step1_introduction()
    elif st.session_state.current_step == 2:
        step2_blog_intro()
    elif st.session_state.current_step == 3:
        step3_image_selection()
    elif st.session_state.current_step == 4:
        step4_bgm_selection()
    elif st.session_state.current_step == 5:
        step5_quotation()
    elif st.session_state.current_step == 6:
        step6_your_rights()
    elif st.session_state.current_step == 7:
        step7_final_quiz()
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.current_step > 1:
            if st.button("⬅️ 前へ"):
                st.session_state.current_step -= 1
                st.rerun()
    
    with col3:
        if st.session_state.current_step < len(step_names):
            if st.button("次へ ➡️"):
                st.session_state.current_step += 1
                st.rerun()

def step1_introduction():
    st.header("ステップ1: はじめに - きみの「作品」は宝物だ！💎")
    
    st.markdown("""
    **著作権クエストへようこそ！**
    
    あなたが描いた絵、書いた文章、撮った写真。それらはすべて、あなただけの「著作物」という宝物です。
    
    著作権は、その宝物を他人に勝手に使われないように、法律が自動的に守ってくれる権利のことです。
    
    クリエイターとして知っておくべきルールを、ブログを作りながら学んでいきましょう！
    """)
    
    # Visualization: What is copyright?
    fig = go.Figure(data=[
        go.Bar(
            x=['あなたの絵', 'あなたの文章', 'あなたの写真', 'あなたの音楽'],
            y=[100, 100, 100, 100],
            marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'],
            text=['🎨', '📝', '📷', '🎵'],
            textposition='inside',
            textfont=dict(size=30)
        )
    ])
    
    fig.update_layout(
        title="あなたが作ったものは全て「著作物」= 法律が守る宝物！",
        yaxis_title="保護レベル (%)",
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def step2_blog_intro():
    st.header("ステップ2: ブログ記事を作ってみよう！")
    
    st.subheader("📝 テーマ：『私の大好きなペット』")
    
    st.markdown("""
    あなたの可愛いペットを紹介するブログ記事を作ります。
    まずは、記事に使う「ペットの画像」を探しましょう。
    
    でも、ネット上の画像を何でも自由に使えるわけではありません。注意して選びましょう！
    """)
    
    st.info("💡 ポイント: インターネット上の画像や音楽、文章には、それを作った人の著作権があります。")

def step3_image_selection():
    st.header("ステップ3: 画像さがし - この画像、使える？使えない？🖼️")
    
    st.subheader("どの画像を選ぶ？ 著作権チェック！")
    
    st.markdown("""
    ブログのトップ画像にしたい犬の写真。以下の3つの選択肢のうち、
    あなたのブログで自由に使えるのはどれでしょう？
    """)
    
    tab1, tab2, tab3 = st.tabs(["A: 有名アニメの犬", "B: 100年以上前の絵画", "C: あるカメラマンの写真"])
    
    with tab1:
        st.markdown("### 🐕 有名アニメの犬")
        st.markdown("人気アニメのキャラクターの画像")
        
        if st.button("この画像を使う", key="anime_dog"):
            st.error("""
            ❌ **使えません！**
            
            これは有名なキャラクターで、強力な著作権で守られています。
            作者に無断でWebページに掲載すると、著作権の一つである「公衆送信権」の侵害になります。
            """)
    
    with tab2:
        st.markdown("### 🖼️ 100年以上前の絵画")
        st.markdown("古典的な犬の絵画")
        
        if st.button("この絵を使う", key="classic_painting"):
            st.success("""
            ✅ **使えます！**
            
            作者が亡くなってから長い年月が経ち、著作権の保護期間が終了しています。
            このような作品は**パブリック・ドメイン**と呼ばれ、誰でも自由に利用できます。
            """)
    
    with tab3:
        st.markdown("### 📷 あるカメラマンの写真")
        st.markdown("CC BY ライセンスの写真")
        
        if st.button("この写真を使う", key="cc_photo"):
            st.success("""
            ✅ **条件付きで使えます！**
            
            これは**クリエイティブ・コモンズ（CC）**という「この条件を守れば自由に使っていいですよ」という意思表示です。
            「BY」は「作者の名前を表示すること（表示）」が条件です。
            """)

def step4_bgm_selection():
    st.header("ステップ4: BGM選び - この曲、流せる？流せない？🎵")
    
    st.subheader("記事紹介動画のBGMを選ぼう！")
    
    st.markdown("""
    次に、ブログを紹介する短い動画にBGMを付けたいと思います。
    どちらの曲が使えますか？
    """)
    
    choice = st.radio(
        "どちらの曲を選びますか？",
        ["① バッハ作曲のクラシック音楽（作曲家は1750年没）", 
         "② 今、大人気のアイドルの最新曲"]
    )
    
    if choice:
        st.markdown("---")
        if "バッハ" in choice:
            st.success("""
            ✅ **正解です！**
            
            バッハのように、作者の死後、著作権の保護期間が切れた楽曲は**パブリック・ドメイン**となり、自由に利用できます。
            """)
        else:
            st.error("""
            ❌ **これは使えません！**
            
            最新のヒット曲は、作詞家・作曲家の著作権や、歌手・演奏家の**著作隣接権**で保護されているため、
            無断で利用することはできません。
            """)
    
    # Visualization of copyright duration
    if choice:
        current_year = 2025
        
        # バッハのケース（1750年没 → 1820年まで保護）
        bach_death = 1750
        bach_protection_end = bach_death + 70
        
        # 現代アイドルのケース（現在活動中）
        idol_start = 2000  # 活動開始年
        
        fig = go.Figure()
        
        # バッハの保護期間（2つのセグメントに分ける）
        fig.add_trace(go.Bar(
            name='バッハ（1750年没）',
            y=['バッハ'],
            x=[bach_protection_end - bach_death],
            base=[bach_death],
            orientation='h',
            marker_color='red',
            text='保護期間 (1750-1820年)',
            textposition='inside',
            showlegend=False,
            hovertemplate='バッハ<br>1750-1820年: 保護期間中<extra></extra>'
        ))
        
        fig.add_trace(go.Bar(
            name='バッハ（1750年没）',
            y=['バッハ'],
            x=[current_year - bach_protection_end],
            base=[bach_protection_end],
            orientation='h',
            marker_color='green',
            text='パブリック・ドメイン (1820年以降)',
            textposition='inside',
            showlegend=False,
            hovertemplate='バッハ<br>1820年以降: パブリック・ドメイン<extra></extra>'
        ))
        
        # 現代アイドルの保護期間
        fig.add_trace(go.Bar(
            name='現代のアイドル',
            y=['現代アイドル'],
            x=[current_year - idol_start],
            base=[idol_start],
            orientation='h',
            marker_color='red',
            text='著作権保護期間中 (2000年以降)',
            textposition='inside',
            showlegend=False,
            hovertemplate='現代アイドル<br>2000年以降: 著作権保護期間中<extra></extra>'
        ))
        
        fig.update_layout(
            title="著作権の保護期間タイムライン（西暦表示）",
            xaxis_title="西暦",
            yaxis_title="",
            height=300,
            xaxis=dict(range=[1740, 2040]),
            showlegend=False
        )
        
        # 重要な年を示す縦線を追加
        fig.add_vline(x=bach_protection_end, line_dash="dot", line_color="orange", 
                      annotation_text="1820年<br>保護終了")
        fig.add_vline(x=current_year, line_dash="dash", line_color="blue", 
                      annotation_text=f"現在<br>({current_year}年)")
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **グラフの見方：**
        - 🔴 赤い部分：著作権保護期間（利用制限あり）
        - 🟢 緑の部分：保護期間終了（自由利用可能）
        - 📅 青い線：現在（2025年）
        - 🟠 オレンジ線：バッハの保護期間終了（1820年）
        """)
        
        st.warning("""
        **重要な注意点：**
        
        📝 **楽曲の著作権**と**演奏・録音の著作隣接権**は別物です：
        
        - **バッハの楽曲自体**：パブリック・ドメイン（自由利用可能）
        - **現代の演奏・録音**：演奏者や録音会社に著作隣接権があり、保護期間中（通常50～70年）
        
        つまり、バッハの楽譜は自由に使えますが、**特定の演奏録音を使う場合は演奏者・録音会社の許可が必要**です。
        """)

def step5_quotation():
    st.header("ステップ5: ルールを守って「引用」しよう！📚")
    
    st.subheader("ペットに関する豆知識を紹介しよう")
    
    st.markdown("""
    本で読んだ豆知識を、ブログで紹介したくなりました。
    正しい紹介の仕方はどちらでしょう？
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        ### ❌ ダメな例
        
        **犬の豆知識**
        
        犬の嗅覚は人間の100万倍以上と言われている。
        
        *（まるで自分が書いた文章のように見せてしまっている）*
        """)
    
    with col2:
        st.success("""
        ### ✅ 良い例
        
        **犬の豆知識**
        
        書籍『犬のひみつ』（田中太郎 著）には、次のように書かれています。
        
        > 犬の嗅覚は人間の100万倍以上と言われている。
        
        **出典：『犬のひみつ』**
        """)
    
    st.info("""
    **解説**
    
    右側が良い例です。
    他人の文章を、**出典を明記して**、自分の文章と区別がつくように用いることを**引用**といい、
    これは著作権の例外規定として認められています。
    """)

def step6_your_rights():
    st.header("ステップ6: きみの権利を知り、意思表示をしよう！")
    
    st.subheader("🎉 あなたのブログ記事を公開！")
    
    st.markdown("""
    おめでとうございます！あなたのブログ記事が完成しました。
    今度は、あなたがこの記事の「**著作権者**」です。
    
    著作権には、大きく分けて「心（人格）」に関する権利と、「財産」に関する権利があります。
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💖 著作者人格権")
        st.markdown("**クリエイターの「心」を守る権利**")
        st.markdown("作者としてのプライドや、作品への思い入れを守る権利です。他人に譲ることはできません。")
        
        st.success("✅ 勝手に内容を変えられない！（同一性保持権）")
        st.success("✅ 作者として名前を出すか決められる！（氏名表示権）")
    
    with col2:
        st.markdown("### 💰 著作権（財産権）")
        st.markdown("**クリエイターの「財産」を守る権利**")
        st.markdown("作品の利用を許可してお金を得るなど、財産的な利益を守る権利です。")
        
        st.warning("⚠️ 勝手にコピーさせない！（複製権）")
        st.warning("⚠️ 勝手にネットで使わせない！（公衆送信権）")
    
    st.subheader("🏷️ あなたの作品に利用ルールを付けよう！")
    
    st.markdown("""
    これらの権利をもとに、他の人にあなたの記事をどのように使ってもらいたいか、
    **クリエイティブ・コモンズ**で意思表示をしてみましょう。
    """)
    
    selected_rules = st.multiselect(
        "あなたの作品に付ける利用ルールを選んでください:",
        [
            "BY: 私の名前を表示してほしい（氏名表示権の尊重）",
            "ND: 内容を勝手に変えないでほしい（同一性保持権の尊重）", 
            "NC: お金儲けには使わないでほしい（財産権の主張）"
        ]
    )
    
    if selected_rules:
        st.markdown("---")
        st.subheader("🏆 あなたが選んだライセンス")
        
        rules_short = []
        if "BY:" in str(selected_rules):
            rules_short.append("BY")
        if "ND:" in str(selected_rules):
            rules_short.append("ND") 
        if "NC:" in str(selected_rules):
            rules_short.append("NC")
            
        license_name = "CC " + "-".join(rules_short) if rules_short else "CC 0"
        
        st.success(f"**{license_name}** ライセンス")
        st.markdown("このマークを付けておけば、あなたの意思が世界中の人に伝わります！")

def step7_final_quiz():
    st.header("ステップ7: 最終確認！これってOK？")
    
    st.subheader("📚 私的利用と著作権")
    
    st.markdown("""
    **問題：** あなたは勉強のために、買ったばかりの問題集をコピーすることにしました。
    法律的にOKなのはどっち？
    """)
    
    choice = st.radio(
        "正しいのはどっち？",
        [
            "① 自分の勉強用に1部だけコピーする",
            "② クラスメイト全員の分も、まとめてコピーしてあげる"
        ]
    )
    
    if choice:
        st.markdown("---")
        if "自分の勉強用" in choice:
            st.success("""
            ✅ **正解です！**
            
            自分自身や家族など、限られた範囲で利用するためにコピーすることは
            「**私的利用における複製**」として認められています。
            """)
        else:
            st.error("""
            ❌ **これはNGです！**
            
            友達の分までコピーして配るのは、私的利用の範囲を超えてしまうため
            著作権侵害にあたります。
            """)
    
    # Final completion message
    if st.session_state.current_step == 7 and choice:
        st.markdown("---")
        st.balloons()
        st.success("""
        ### 🎊 著作権クエスト完了！おめでとうございます！
        
        あなたは著作権の基本的なルールを学びました：
        
        - 作品には自動的に著作権が発生すること
        - 他人の作品を使うときのルール
        - 正しい引用の方法
        - あなた自身の権利について
        - 私的利用の範囲
        
        これからも、クリエイターとして、そして他の人の作品を利用する人として、
        著作権を尊重していきましょう！
        """)

if __name__ == "__main__":
    main()