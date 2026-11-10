---
title: 'Beyond Modality Preference: Controlling Multimodal Arbitration under Modality
  Conflict in MLLMs'
title_zh: 多模态大模型模态冲突场景下的模态仲裁控制方法
authors:
- Zhaoying Pan
- Shenyu Lu
- Jun Hui Wong
- Junyi Chai
- Xiaoqian Wang
affiliations:
- Purdue University
arxiv_id: '2611.12883'
url: https://arxiv.org/abs/2611.12883
pdf_url: https://arxiv.org/pdf/2611.12883
published: '2026-11-09'
collected: '2026-11-10'
category: Multimodal
direction: 多模态大模型 · 模态冲突仲裁控制
tags:
- MLLM
- Modality Conflict
- Attention Head
- Inference-time Intervention
- Hallucination Mitigation
one_liner: 通过定位干预少量仲裁注意力头，实现MLLM模态冲突下无需训练的双向可信模态控制
practical_value: '- 电商多模态搜索/推荐场景下，商品图与标题/属性冲突时，可指定优先信任模态（如正品校验优先信任实拍图、活动期优先信任价格文本），无需微调模型即可降低错误率

  - 多模态Agent调用外部多源异构图文检索结果时，仅需10个以内冲突样本标定仲裁头，即可动态指定可信模态，解决跨源信息冲突导致的回答错误

  - 生成式商品文案/海报生成场景下，输入文本要求与参考视觉元素冲突时，可定向强化目标模态注意力，避免生成不符合要求的内容，无需额外prompt工程

  - 工程实现上仅需干预Top30左右高影响注意力头，推理开销极低，可直接集成到现有MLLM推理链路，不影响响应速度'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
MLLM在图文信息冲突时存在固有模态偏好，无法匹配业务指定的可信模态优先级；现有prompt引导可控性差，直接丢弃某一模态又会损失互补信息增益，亟需无需训练的推理时模态仲裁控制方案。

### 方法关键点
- 通过激活补丁法定位仲裁注意力头：基于10个左右冲突样本，计算不同注意力头对模态偏好的因果影响得分，筛选Top30高得分头作为干预靶点
- 推理时无训练干预：对仲裁头的预softmax注意力得分加权偏移，正向增强目标模态token的注意力权重，负向抑制竞争模态权重，支持双向模态切换
- 可选自适应控制：通过图文单模预测logit的余弦相似度检测冲突程度，动态调整干预强度，无冲突时保留多模态互补信息增益

### 关键结果
在MMCD、MC2、CLASH等4个模态冲突基准+PhD幻觉基准上，覆盖Qwen3、LLaVA-OV等4个开源MLLM，对比CAP、MPS等基线：MMCD基准上双向控制准确率达100%，远超MPS的最高99.18%；MC2基准上图像优先时图像准确率达79.5%，较基线47.25%提升32pct，文本优先时文本准确率达86.75%，较基线42.2%提升44pct；仅需10个校准样本定位的仲裁头可跨基准通用，自适应模式在冲突样本占比<20%时，保留多模态推理精度优势，比单模推理高6~8pct。

### 核心结论
MLLM的模态仲裁行为由极少量注意力头决定，仅需对这些头做推理时轻量干预，即可实现高可控的模态优先级控制，无需微调或额外训练。
