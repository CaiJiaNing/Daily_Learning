shopping_cart = []  # 购物车列表，每个元素是一个字典

print("Welcome!\n")

while True:
    user_input_number = input(
        "1:添加购物车\n"
        "2:修改购物车\n"
        "3:删除购物车\n"
        "4:查询购物车\n"
        "5:退出购物车\n"
        "请输入选项: "
    )

    match user_input_number:
        # ========== 1. 添加商品 ==========
        case "1":
            name = input("商品名称: ").strip()
            if not name:
                print("商品名称不能为空！")
                continue

            # 校验价格
            try:
                price = float(input("商品价格: "))
                if price < 0:
                    print("价格不能为负数！")
                    continue
            except ValueError:
                print("价格必须是数字！")
                continue

            # 校验数量
            try:
                quantity = int(input("商品数量: "))
                if quantity <= 0:
                    print("数量必须是正整数！")
                    continue
            except ValueError:
                print("数量必须是整数！")
                continue

            item = {
                "name": name,
                "price": price,
                "quantity": quantity
            }
            shopping_cart.append(item)
            print(f"已添加：{name}，单价 {price}，数量 {quantity}")

        # ========== 2. 修改商品 ==========
        case "2":
            if not shopping_cart:
                print("购物车为空，无法修改！")
                continue

            target_name = input("请输入要修改的商品名称: ").strip()
            found = False
            for item in shopping_cart:
                if item["name"] == target_name:
                    found = True
                    print(f"当前商品：{item['name']}，单价 {item['price']}，数量 {item['quantity']}")
                    # 修改价格
                    new_price = input("请输入新价格（直接回车跳过）: ").strip()
                    if new_price:
                        try:
                            new_price = float(new_price)
                            if new_price < 0:
                                print("价格不能为负数！")
                            else:
                                item["price"] = new_price
                        except ValueError:
                            print("价格必须是数字，修改价格失败。")
                    # 修改数量
                    new_quantity = input("请输入新数量（直接回车跳过）: ").strip()
                    if new_quantity:
                        try:
                            new_quantity = int(new_quantity)
                            if new_quantity <= 0:
                                print("数量必须是正整数！")
                            else:
                                item["quantity"] = new_quantity
                        except ValueError:
                            print("数量必须是整数，修改数量失败。")
                    print("修改完成！")
                    break
            if not found:
                print(f"未找到商品：{target_name}")

        # ========== 3. 删除商品 ==========
        case "3":
            if not shopping_cart:
                print("购物车为空，无法删除！")
                continue

            target_name = input("请输入要删除的商品名称: ").strip()
            found = False
            for i, item in enumerate(shopping_cart):
                if item["name"] == target_name:
                    del shopping_cart[i]
                    found = True
                    print(f"已删除商品：{target_name}")
                    break
            if not found:
                print(f"未找到商品：{target_name}")

        # ========== 4. 查询购物车 ==========
        case "4":
            if not shopping_cart:
                print("购物车为空。")
            else:
                print("\n===== 购物车清单 =====")
                total = 0.0
                for i, item in enumerate(shopping_cart, 1):
                    subtotal = item["price"] * item["quantity"]
                    total += subtotal
                    print(f"{i}. {item['name']}  单价：{item['price']}  数量：{item['quantity']}  小计：{subtotal:.2f}")
                print(f"总计：{total:.2f}")
                print("=====================\n")

        # ========== 5. 退出 ==========
        case "5":
            print("退出购物车，再见！")
            break

        # ========== 无效选项 ==========
        case _:
            print("无效选项，请重新输入！")