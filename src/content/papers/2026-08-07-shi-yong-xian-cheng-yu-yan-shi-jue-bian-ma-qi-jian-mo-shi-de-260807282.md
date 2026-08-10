---
title: Gaze Behavior in Visual World Experiments Can be Modeled With Off-the-shelf
  Language-Vision Encoders
title_zh: 使用现成语言-视觉编码器建模视觉世界实验中的注视行为
authors:
- Rahul Murali Shankar
- Titus von der Malsburg
- Sebastian Padó
affiliations:
- University of Stuttgart, Germany
arxiv_id: '2608.07282'
url: https://arxiv.org/abs/2608.07282
pdf_url: https://arxiv.org/pdf/2608.07282
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态认知建模 · 零样本注视行为预测
tags:
- CLIP
- Multimodal Encoder
- Zero-shot
- Gaze Prediction
- Bi-encoder
one_liner: 结合CLIP类双编码器与双模态归因方法，零微调实现视觉世界实验中人类注视行为的准确预测
practical_value: '- 电商多模态搜索/推荐场景可复用CLIP类双编码器+归因方法的轻量架构，无需微调即可实现跨模态语义对齐，降低落地成本

  - 直播/短视频电商的用户兴趣预判场景，可参考注视行为预测逻辑，结合用户视线停留、画面关注区域数据优化实时推荐排序策略

  - 多模态交互Agent的环境感知模块可借鉴该双模态归因方法，提升自然语言指令与视觉场景内容的匹配精度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前计算心理语言学领域的大模型应用研究多聚焦单模态文本/语音处理场景，普遍忽略了视觉与语言输入同步的多模态实验范式，视觉世界研究中人类注视行为的预测方案普遍需要定制训练、落地成本高。
### 方法关键点
采用CLIP家族的轻量多模态双编码器架构，搭配双模态归因方法，整个流程不引入生成式结构，不需要针对注视预测任务做微调，也无需额外的任务相关预训练。
### 关键结果
可鲁棒复现经典英文视觉世界研究中人类预测性加工的实验结论，无需微调的前提下，预测表现与定制化训练的有监督基线模型持平，可准确还原人类注视行为的分布规律。
