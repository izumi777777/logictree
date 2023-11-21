# ロジカルシンキングのピラミッドストラクチャーツリーを作成するPythonアプリケーションです

# =====================================================================
# ライブラリの宣言
# =====================================================================

from node import Node

# =====================================================================
# 本アプリケーションコード
# =====================================================================

def create_pyramid_structure():
    # テーマの入力とルートノードの作成
    theme = input("テーマを入力してください: ")
    root = Node(theme)
    
    # 要素の再帰的な構築
    build_structure(root)
    return root

def build_structure(node):
    # ユーザーに対して関連する要素を入力させ、子ノードとして追加
    add_element = ask_question(f"「{node.data}」に関連する要素を入力してください (空白で終了): ")
    while add_element:
        child_node = Node(add_element)
        node.children.append(child_node)
        # 子ノードに対して再帰的に同じプロセスを繰り返す
        build_structure(child_node)
        add_element = ask_question(f"「{node.data}」に関連する要素を入力してください (空白で終了): ")

def ask_question(question):
    # ユーザーに対して質問を表示し、回答を受け取る
    answer = input(question + " ")
    return answer.strip()  # 入力の前後の余白を削除

def display_tree(node, level=0):
    # ツリーを階層付きで表示
    print("  " * level + "└─ " + node.data)
    if node.children:
        for child in node.children:
            display_tree(child, level + 1)

def main():
    print("テーマに関連する要素を入力してください。空白の入力で終了します。")
    # ピラミッド構造の作成と表示
    root = create_pyramid_structure()
    print("\n作成したピラミッド構造:")
    display_tree(root)

if __name__ == "__main__":
    main()
