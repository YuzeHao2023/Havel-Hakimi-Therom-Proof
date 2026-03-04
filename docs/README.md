# GitHub Pages 部署说明

## 启用 GitHub Pages

这个项目的 Demo 网站位于 `/docs` 文件夹，已配置为用 GitHub Pages 部署。

### 启用步骤

1. **进入仓库设置**: 在 GitHub 上打开你的仓库，点击 "Settings"

2. **找到 Pages 选项**: 在左侧菜单中找到 "Pages" 选项（通常在 "Code and automation" 部分）

3. **配置部署源**:
   - 在 "Build and deployment" 下，选择 "Source" 为 "Deploy from a branch"
   - 选择分支为 `main`（或你的默认分支）
   - 选择文件夹为 `/docs`
   - 点击 "Save"

4. **等待部署**: GitHub 会自动构建并部署你的网站。在 Pages 部分你会看到部署状态。

5. **访问你的网站**: 部署完成后，你会看到你的网站 URL，通常格式为：
   ```
   https://YuzeHao2023.github.io/Havel-Hakimi-Therom-Proof/
   ```

## 文件结构

```
docs/
├── index.html                 # 主页
├── css/
│   └── style.css             # 样式表
├── js/
│   └── game.js               # 游戏逻辑和交互
└── img/                        # 图片文件夹（暂时为空）
```

## 功能

网站包含以下内容：

1. **介绍**: Havel-Hakimi 定理的快速介绍
2. **定义**: 定理的正式定义和规约过程
3. **定理陈述**: 定理的完整陈述
4. **证明**: 详细的数学证明（充分性和必要性）
5. **算法**: Havel-Hakimi 算法的实现和复杂度分析
6. **交互游戏**: 用户可以互动的图构造游戏
7. **示例**: 具体的实例和应用领域
8. **参考资源**: 相关文献和在线资源

## 游戏说明

在游戏中：
- 系统随机生成一个可图的度序列
- 每个节点显示它需要的边数
- 通过拖动连接节点来添加边
- 当所有节点的度数都达到目标时，游戏成功
- 点击"重置"按钮重新开始

## 在本地运行

你也可以在本地运行这个网站。只需用你喜欢的方式启动一个本地服务器：

### 使用 Python 3
```bash
cd docs
python -m http.server 8000
```

### 使用 Node.js (http-server)
```bash
npm install -g http-server
cd docs
http-server
```

### 使用其他服务器
任何支持静态文件的 HTTP 服务器都可以。

然后在浏览器中访问 `http://localhost:8000`

## 自定义

你可以通过以下方式自定义网站：

- **样式**: 编辑 `css/style.css` 修改外观
- **内容**: 编辑 `index.html` 更新文本和信息
- **游戏**: 编辑 `js/game.js` 修改游戏逻辑

## 支持的浏览器

- Chrome (最新版本)
- Firefox (最新版本)
- Safari (最新版本)
- Edge (最新版本)

## 技术栈

- HTML5
- CSS3
- JavaScript (Vanilla JS + D3.js)
- MathJax (用于数学公式渲染)

## 许可证

请参考项目根目录的 LICENSE 文件。

## 问题反馈

如有任何问题或建议，欢迎提交 Issue 或 Pull Request。
