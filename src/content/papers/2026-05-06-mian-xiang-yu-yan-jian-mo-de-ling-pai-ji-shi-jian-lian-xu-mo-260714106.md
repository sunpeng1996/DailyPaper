---
title: Token Time Continuous Diffusion for Language Modeling
title_zh: 面向语言建模的令牌级时间连续扩散（TTCD）模型
authors:
- Parikshit Bansal
- Sujay Sanghavi
affiliations:
- UT Austin
arxiv_id: '2607.14106'
url: https://arxiv.org/abs/2607.14106
pdf_url: https://arxiv.org/pdf/2607.14106
published: '2026-05-06'
collected: '2026-07-18'
category: LLM
direction: 连续扩散语言建模 · 少步生成优化
tags:
- Diffusion LM
- Continuous Diffusion
- Fast Generation
- Flow Matching
- Token-wise Modeling
one_liner: 提出带令牌级独立时间步的连续扩散语言模型，少步生成性能远超各类基线
practical_value: '- 低延迟生成场景直接复用：电商搜索suggestion、商品短标题生成、推荐理由生成等高QPS场景，可直接替换现有离散扩散模型，2-4步即可达到之前8步以上的生成质量，延迟减半以上

  - 条件生成工程改造trick：做前缀条件生成（比如给定用户历史生成推荐文案、给定Query生成相关搜索词）时，直接将前缀token的时间固定为1，无需额外处理prompt，改造成本远低于需要时间翘曲的单全局时间扩散模型

  - 熵驱动秩分配思路可迁移：在生成式推荐生成item属性、多模态商品文案时，可按token/属性的确定性（比如品类、价格确定性高，个性化文案确定性低）分配去噪优先级，提升整体生成准确率，减少逻辑矛盾

  - 无新增参数的adaLN改造：现有DiT架构的扩散模型，只需修改adaLN的时间输入为token级即可支持per-token时间，无额外参数量上涨，适合线上资源受限的服务部署'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
离散扩散语言模型少步生成时，多token并行采样会引入因子分解误差，生成质量骤降；现有连续扩散模型采用单全局时间，无法区分不同token的生成难度，也不能自然适配条件生成场景（prompt和待生成部分噪声状态完全不同），导致少步条件生成性能差、生成多样性低，易出现重复生成问题。

### 方法关键点
- 引入全局时间+per-token局部时间双轨设计，每个token根据分配的秩独立推进去噪进度，高秩（确定性高）的token去噪更快，所有token的局部时间均值等于全局时间，无需额外时间翘曲
- 基于初始前向传播的输出熵分配token秩，熵越低确定性越高，分配越高的秩，固定后全程无需调整
- 仅修改DiT的adaLN层，用每个token的局部时间生成调制参数，不新增任何模型参数
- 支持自蒸馏为shortcut模型，进一步压缩生成步数

### 关键实验结果
在OpenWebText（160M参数）、Sudoku 9x9、QM9分子生成数据集上，对比MDLM、Duo、FLM等主流扩散LM基线：Sudoku 2步生成准确率达31.51%，比离散熵排序基线高近20pp，比单时间连续基线高31pp；条件生成场景下，2-4步生成的PPL比基线低15%以上，同时生成熵更高（多样性更好），有效避免重复生成问题。

### 核心结论
为每个token分配独立去噪进度，是提升少步扩散生成质量、适配条件生成场景的低成本高效方案
