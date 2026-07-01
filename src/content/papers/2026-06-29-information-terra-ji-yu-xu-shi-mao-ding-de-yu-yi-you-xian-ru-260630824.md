---
title: 'Information Terra: A Narrative-Anchored Semantic-First Projection of Document
  Embeddings'
title_zh: Information Terra：基于叙事锚定的语义优先文档嵌入投影方法
authors:
- Brian Keith-Norambuena
- Fausto German
- Chris North
affiliations:
- Universidad Católica del Norte, Chile
- Virginia Tech
arxiv_id: '2606.30824'
url: https://arxiv.org/abs/2606.30824
pdf_url: https://arxiv.org/pdf/2606.30824
published: '2026-06-29'
collected: '2026-07-01'
category: Other
direction: 文档嵌入 · 语义投影 · 叙事可视化
tags:
- Document Embedding
- Semantic Projection
- Narrative Visualization
- Kernel Density Estimation
one_liner: 提出叙事锚定的语义优先文档嵌入类地球体投影方法，可直观呈现叙事进度与主题偏差
practical_value: '- 做电商商品/品牌舆情时序分析时，可借鉴该语义锚定投影方法，选定大促/事件首尾节点，快速梳理舆情演化脉络与主题偏移

  - 做内容池/商品池主题聚类可视化时，可复用其基于嵌入密度的核密度估计方法识别主题区域，配合小模型自动生成主题标签

  - 做推荐系统可解释性分析时，可将用户行为序列对应的内容/商品嵌入按该方法投影，直观呈现用户兴趣演化路径与偏离度'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有文档嵌入降维投影方法的轴缺乏语义可解释性，无法直观呈现叙事类文本的逻辑进度与主题偏移关系，难以支撑长周期事件脉络的快速梳理。
**方法关键点**：1. 以用户指定的两个端点文档作为类地球球体南北极，两点在嵌入超球面的测地线作为本初子午线，纬度编码叙事进度、经度编码主题偏差；2. 用核密度估计基于文档嵌入分布识别主题区域，配合小模型自动生成主题标签；3. 基于叙事一致性图构建满足测地线进度单调约束的叙事路径，输出可读性强的故事线。
**关键结果**：在540篇古巴抗议相关文章的语料上验证，可清晰还原从2016年奥巴马访古到2021年抗议期间国际援助的完整叙事脉络。
