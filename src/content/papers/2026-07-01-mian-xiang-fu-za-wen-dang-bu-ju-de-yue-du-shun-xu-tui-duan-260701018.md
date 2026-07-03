---
title: Reading Order Inference for Complex Document Layouts
title_zh: 面向复杂文档布局的阅读顺序推断
authors:
- Iddo Hakim
- Sharva Gogawale
- Omer Ventura
- Gal Grudka
- Daria Vasyutinsky-Shapira
- Berat Kurar-Barakat
- Nachum Dershowitz
affiliations:
- School of Computer Science and AI, Tel Aviv University
arxiv_id: '2607.01018'
url: https://arxiv.org/abs/2607.01018
pdf_url: https://arxiv.org/pdf/2607.01018
published: '2026-07-01'
collected: '2026-07-03'
category: Other
direction: 文档布局分析 · 无训练阅读顺序推断
tags:
- Reading Order Inference
- Document Layout Analysis
- Training-free
- Graph-based Method
- Max-regret Inference
one_liner: 提出无训练图式框架与max-regret推理规则，解决非矩形交错布局的阅读顺序推断问题，效果远超现有基线
practical_value: '- 电商商详OCR结构化场景可复用无训练图+轻量LM信号思路，解决主文绕插图/表格的复杂布局内容顺序抽取问题

  - 多模态RAG的文档预处理环节可替换XY-cut算法，提升非规则多栏/交错布局文档的内容拼接准确率，降低RAG幻觉

  - 存在级联错误的序列决策场景可借鉴max-regret推理规则，优先选择高机会成本的决策，减少错误传导'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
复杂交错布局（如中心文本被环绕注释的历史手稿）的文档数字化中，现有XY-cut、LayoutReader等方法存在布局适配差、粒度不匹配、镜像鲁棒性低等问题，阅读顺序推断是核心瓶颈。
### 方法关键点
构建无训练的图式框架，将OCR文本行作为有向候选转移图节点，边打分采用因果LM条件似然 + BERT NSP的加权集成（句嵌入信号无增益），全局阅读顺序转化为度约束有向路径覆盖问题；提出max-regret推理规则，优先选择高机会成本的边，避免贪心选择的级联「边窃取」错误。
### 关键结果
环绕式Glossa布局上平均恢复95%的真实后继边，远超XY-cut的50%；OmniDocBench多栏子集宏边准确率达88%，优于XY-cut的75%、LayoutReader的25%；水平/垂直镜像下性能波动<1pp，远低于LayoutReader的8pp波动。
