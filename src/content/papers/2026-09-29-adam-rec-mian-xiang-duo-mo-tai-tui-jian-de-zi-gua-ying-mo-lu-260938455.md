---
title: 'AdaM-Rec: Adaptive Modality Routing for Multimodal Recommendation'
title_zh: AdaM-Rec：面向多模态推荐的自适应模态路由框架
authors:
- Honghao Fu
- Jiacheng Chen
- Manxi Lin
- Junjun Zheng
- Xiangheng Kong
- Yiwei Wang
- Xin Yu
- Miao Xu
- Yuning Jiang
- Yujun Cai
affiliations:
- University of Queensland
- Alibaba Group
- Southeast University
- University of Adelaide
arxiv_id: '2609.38455'
url: https://arxiv.org/abs/2609.38455
pdf_url: https://arxiv.org/pdf/2609.38455
published: '2026-09-29'
collected: '2026-10-01'
category: RecSys
direction: 多模态推荐 · 自适应模态路由
tags:
- MultimodalRec
- ModalityRouting
- LLM4Rec
- AgenticRec
- E-commerce
one_liner: 基于LLM的多模态推荐框架，动态分配文本/多模态召回权重，适配不同用户查询意图
practical_value: '- 电商多模态搜索推荐场景可直接复用模态路由逻辑：对鞋服、家居等外观导向类查询加大多模态召回权重，对3C配件、家电等功能导向类查询加大文本召回权重，减少视觉噪声引入

  - 可落地伪query自验证机制：基于用户历史正向交互商品生成与当前查询粒度匹配的伪query，无需人工标注即可在线验证不同召回策略的效果，个性化优化召回配置

  - 工程落地可优先采用高性价比配置：文本编码器选用0.6B小模型、多模态编码器选用2B级模型即可获得最优效率/效果trade-off，无需盲目使用大模型增加推理成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态推荐普遍采用静态模态融合策略，默认文本和视觉信号的重要性在所有场景下一致，但实际电商场景中不同查询对模态的依赖差异极大：外观导向的查询（如带波浪厚底的运动鞋）需要大量视觉信号，功能导向的查询（如70W MacBook USB-C充电器）过多引入视觉信号反而会召回外观相似但功能不符的噪声，导致推荐效果下降。

### 方法关键点
- 离线层：用MLLM将商品图文信息转换成结构化文本profile，基于用户历史交互生成结构化偏好profile，构建包含文本、多模态双embedding的商品库和用户偏好库，召回相似用户的历史路由参数作为初始先验
- 自适应模态路由层：基于当前查询和用户历史正向交互商品，生成与真实查询粒度匹配的伪query，分别测试双召回分支在伪query任务上的召回效果，迭代优化文本/多模态召回的权重分配和总召回预算，优化后的参数写回用户库作为后续协同先验
- 推荐层：按优化后的权重执行双路召回，补充相似用户的正向交互商品作为协同召回补充，最后用LLM基于查询、用户偏好、商品profile做相关性打分排序

### 关键实验
在亚马逊3个查询式推荐数据集（美妆、服饰鞋靴、音乐）上，对比11个SOTA基线，HR@40平均提升14.1%，NDCG@40平均提升15.9%；在2个偏好式序列推荐数据集（视频游戏、母婴）上也取得SOTA级效果。消融实验显示去掉自适应路由后HR@40下降13.4%，验证了动态路由的核心价值。

最值得记住的一句话：多模态推荐的核心不是最大化模态信息的使用，而是基于查询意图和用户偏好动态选择最匹配的模态信号，避免无效信息引入的噪声。
