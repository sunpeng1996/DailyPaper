---
title: 'CritICL: Inference-Time Weak-to-Strong Generalization from Small Language
  Model Failure Modes'
title_zh: CritICL：利用小模型失败模式实现推理时弱到强泛化
authors:
- Yufan Wu
- Yinghui He
- Zhengyi Hu
- Lang Wei
- Ruichen Li
- Qifan Yang
- Ting Zhu
affiliations:
- The Ohio State University
- Princeton University
arxiv_id: '2608.27455'
url: https://arxiv.org/abs/2608.27455
pdf_url: https://arxiv.org/pdf/2608.27455
published: '2026-08-27'
collected: '2026-08-28'
category: Reasoning
direction: 大模型推理优化 · 弱到强泛化
tags:
- ICL
- Weak-to-Strong Generalization
- Inference Optimization
- Failure Mode
- Prompt Engineering
one_liner: 基于小模型结构化失败模式构建CritBank，通过双检索策略低开销提升大模型推理性能
practical_value: '- 电商/推荐场景下使用同基座LLM做文案生成、query理解时，可先调用小版本模型跑历史请求构建业务专属CritBank，推理时注入对应错误规避提示，替代多轮self-refine流程，可降本20%以上

  - Agent做复杂任务规划时，可离线构建同基座小模型的任务失败知识库，静态版本直接将高频失败坑点加入system prompt，动态版本先预测当前任务潜在失败点再检索规避示例，推理效率远高于多轮self-correction

  - 所有LLM相关业务的ICL示例选择无需仅依赖语义相似，优先选取匹配当前任务高频失败模式的反例+修正说明，效果优于单纯堆砌正确示例，可直接复用在各类提示优化场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有推理时缩放方法（自一致性、自反思、外部校验等）均依赖多次生成或额外模型调用，推理成本居高不下；此前弱到强泛化方法需要小模型实时输出指导，仍存在额外开销，且未充分利用同系列模型失败模式跨尺度高度一致的结构化特性。
### 方法关键点
- 离线构建CritBank：用同系列小模型在目标任务数据集上生成错误回答，调用强LLM为每个错误打失败模式标签、生成自然语言纠错评语，形成包含query、错误回答、失败标签、评语的结构化知识库
- 双推理策略：CritICL-static 离线聚合小模型全局失败模式分布，选取高频失败对应评语作为固定ICL示例，仅需1次大模型生成；CritICL-dynamic 先让大模型预测当前query的潜在失败模式，再检索对应评语作为ICL示例，仅需2次生成
### 关键实验
在GSM8K、MATH、AMC23、AIME等数学推理基准上测试，对比标准ICL、自一致性、自反思、LLM-as-judge等基线。Qwen2.5-72B上CritICL-static Pass@1达59.2%，优于最强基线Consistency@5（59.0%）；总token消耗仅3768，较Consistency@5低21.7%，较自反思低50%。
### 核心结论
同基座小模型的结构化失败模式是可复用的低开销优化资源，投入产出比远高于单纯增加正确ICL示例或多轮生成修正。
