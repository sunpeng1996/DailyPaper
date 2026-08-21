---
title: 'G3Ego: Gaze-Guided Graphs for Egocentric Action Understanding'
title_zh: G3Ego：面向第一人称动作理解的凝视引导图框架
authors:
- Marko Haralović
- Akash Ramakrishnan
- Estefania Talavera Martinez
affiliations:
- University of Zagreb, Faculty of Electrical Engineering and Computing
- University of Twente
arxiv_id: '2608.20157'
url: https://arxiv.org/abs/2608.20157
pdf_url: https://arxiv.org/pdf/2608.20157
published: '2026-08-20'
collected: '2026-08-21'
category: Other
direction: 第一人称动作理解 · 凝视引导图学习
tags:
- Gaze-guided Graph
- Egocentric Action Recognition
- Scene Graph Learning
- Action Anticipation
- Video Understanding
one_liner: 将凝视作为结构线索融入图构建，实现高效可解释的第一人称动作理解
practical_value: '- AR/VR电商场景下，可复用凝视引导图构建思路，识别第一人称视角下用户感兴趣的商品与交互动作，优化实时推荐效果

  - 短视频/直播内容理解场景中，可借鉴凝视剪枝无关实体的思路，过滤用户不关注的背景元素，降低多模态特征计算开销

  - 长尾类识别任务可参考其类不平衡场景下Macro-F1优化逻辑，适配长尾商品/内容的分类召回需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有第一人称动作理解方案依赖外中心数据集预训练的大视频模型，计算开销高；而第一人称动作仅涉及少量手-物交互相关实体，过往凝视仅被用作辅助模态或注意力信号，利用率不足。

### 方法关键点
1. 以凝视作为结构线索直接融入图构建流程，设计G3Ego图架构；
2. 从稀疏采样帧提取视觉语言描述、接地对象、手部线索生成初始动作场景图，再通过用户凝视剪枝无关实体；
3. 时序聚合剪枝后的图嵌入，支撑动作识别与预判任务。

### 关键结果数字
在EGTEA Gaze+、MECCANO数据集上性能比肩主流视频类方法，类不平衡评估场景下Macro-F1稳定提升，无需依赖高成本视频预训练。
