---
title: Self-Reflective Multi-modal Reasoning for Short-Video Fake News Detection
title_zh: 面向短视频虚假新闻检测的自反思多模态推理框架
authors:
- Pinjie Xu
- Yuzhou Yang
- Zhikai Tan
- Qichao Ying
- Zaiyang Yu
- Ce Li
- Zhenxing Qian
affiliations:
- China University of Mining and Technology - Beijing
- Fudan University
- The Institute of Semiconductors of the Chinese Academy of Sciences
arxiv_id: '2608.26787'
url: https://arxiv.org/abs/2608.26787
pdf_url: https://arxiv.org/pdf/2608.26787
published: '2026-08-27'
collected: '2026-08-28'
category: Reasoning
direction: 多模态推理 · 虚假内容风控检测
tags:
- Multimodal Reasoning
- Self-Reflection
- Fake News Detection
- VLM Fine-tuning
- Chain-of-Thought
one_liner: 提出多角色协作自反思、双阶段VLM微调、跨样本校验的短视频虚假新闻检测框架，性能优于现有基线
practical_value: '- 多角色正反推理+仲裁的自反思Prompt框架可直接复用在电商虚假宣传识别、内容风控场景，无需标注CoT数据即可提升推理准确性

  - 双阶段主题自适应VLM微调策略可迁移到垂类多模态内容理解任务，实现低成本垂类适配，降低跨域性能衰减

  - 置信度驱动的同事件跨样本校验方法可用于虚假短视频广告、虚假商品评论识别，通过相似样本交叉验证减少误判'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于LLM/VLM的虚假新闻检测存在三大痛点：无标注CoT监督下自反思推理质量难以提升、优质推理结果无法有效赋能下游模型微调、单样本欺诈模式发现与跨样本校验链路不通。
### 方法关键点
提出SRM-FND自反思多模态推理框架：1. 设计盲分析师、反结论推理器、自一致性仲裁器三模块协作，通过对比审议、迭代根因诊断、提示词修正生成高质量可区分推理逻辑；2. 采用双阶段主题自适应VLM微调，提升多模态对齐能力，实现轻量级主题适配；3. 对低置信度样本，检索同事件可信/可疑样本完成跨样本校验。
### 关键结果
在FakeSV、FakeTT数据集上性能优于所有强基线，预测可解释性更强，跨数据集迁移性能获得显著提升
