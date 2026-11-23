---
title: 'ERA: Embed, Route, Adapt for Cold-Start Cross-Model Latent Retrieval'
title_zh: ERA：冷启动跨模型隐式检索的嵌入、路由、适配框架
authors:
- Venkata Chivukula
- Zifeng Wang
- Jinsung Yoon
affiliations:
- Google
arxiv_id: '2611.26919'
url: https://arxiv.org/abs/2611.26919
pdf_url: https://arxiv.org/pdf/2611.26919
published: '2026-11-20'
collected: '2026-11-23'
category: RecSys
direction: 跨模型检索 · 冷启动适配
tags:
- Cross-Model Retrieval
- Cold Start
- Embedding Alignment
- Adaptive Routing
- Vector Database
one_liner: 无需重索引无标注的冷启动跨模型检索框架，降本提效同时提升检索精度
practical_value: '- 锚点采样优化：用Cosine Farthest Point Sampling替代均匀采样选校准样本，相同锚点预算下跨模型映射精度最高提3倍，适合小样本下的embedding空间对齐场景

  - 对齐损失设计：训练跨空间映射Adapter时叠加Global Orthogonal Regularization，避免小样本下的表示坍缩，无需额外调参，可直接复用在embedding迁移任务

  - 流量降级方案：用极轻量的路由MLP（仅1.2ms overhead）识别难查询，固定预算下优先把算力倾斜给长尾难query，可直接复用在检索系统的成本管控链路

  - 冷启动迁移范式：新embedding模型上线无需全量重索引，仅用少量锚点训练Adapter即可兼容存量向量库，大幅降低模型迭代的迁移成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有向量检索系统的索引与embedding模型强绑定，更换query编码器需要全量重索引，冷启动阶段无查询日志、无人工标注，调用新模型嵌入文档成本高；同时多数迁移方案在小样本下容易出现表示坍缩，长尾难query性能差，无法满足生产级的降本提效需求。

### 方法关键点
- **Embed阶段**：在目标索引的embedding空间用Cosine最远点采样选锚点，优先覆盖空间内的不同语义区域，相同锚点预算下比均匀采样覆盖度提升数倍
- **Adapt阶段**：轻量2层SwiGLU MLP作为Adapter，训练用流形对齐损失（余弦对齐损失+全局正交正则），防止小样本下的表示坍缩，支持冷启动、单域热启动、跨域预训练三级渐进式适配
- **Route阶段**：极轻量开源编码器+2层MLP做路由，预测查询在源/目标模型的检索结果重合度，固定预算下优先路由难query到目标编码器，避免双API调用成本

### 关键实验
在5个BEIR数据集上测试，对比MSE基线、Embedding-Converter基线，nDCG@10相对提升最高35%（Arguana数据集）、12%（FiQA数据集）；20% escalation预算下，端到端查询延迟从原生目标API的160ms降至38-86ms，路由能捕获37.5%的超大性能差距难query，远优于随机路由的0%捕获率。

### 核心结论
跨模型embedding空间迁移的核心是拓扑对齐而非单点精度，小预算下优先覆盖语义边界+兜底长尾查询的性价比最高。
