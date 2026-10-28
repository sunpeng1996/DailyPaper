---
title: 'OpenESM: Energy-Steered Models Are Scalable Foundation Learners'
title_zh: 《OpenESM：能量引导的可扩展通用基础模型架构》
authors:
- Yuan Pu
- Yudong Lu
- Ting Wang
- Zhicong Hong
- Qinuo Li
- Xuansheng Wu
- Na Zou
- Xia Hu
- Guanchu Wang
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.33005'
url: https://arxiv.org/abs/2610.33005
pdf_url: https://arxiv.org/pdf/2610.33005
published: '2026-10-06'
collected: '2026-10-28'
category: LLM
direction: 能量引导大模型 · 通用基础架构
tags:
- Energy-based Model
- Foundation Model
- Open-source LLM
- Scaling Law
- Zero-shot Learning
one_liner: 提出融合能量引导与token生成的ESM架构，零样本性能超越同规模GPT，全栈开源
practical_value: '- 可将能量引导模块嵌入业务域小LLM的预训练/微调流程，通过低能量隐态约束提升生成内容的上下文一致性，适合推荐文案生成、Query改写等场景

  - ESM的注意力掩码并行优化设计可直接复用，大幅降低多位置能量引导的训练开销，适合业务端小样本、低算力下的领域模型迭代

  - 可借鉴能量值评分逻辑构建生成式推荐的质量筛选模块，自动过滤高能量（低语义匹配度）的生成结果，降低内容违规、推荐不相关的概率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统能量基模型（EBM）仅能在单任务/单域落地，无法像GPT类自回归模型一样具备跨域通用能力，核心瓶颈是EBM只能输出能量评分、无法直接生成结构化输出，且大规模训练效率极低，亟需架构创新打通能量引导与通用生成能力的壁垒。

### 方法关键点
- 单架构融合双头部：共享Transformer backbone，同时搭载能量头（输出隐态与上下文的匹配能量值）和生成头（基于低能量隐态生成token）
- 推理流程分两步：先通过K步MCMC梯度下降将初始随机隐态优化到低能量区域，再用优化后隐态引导生成后续token
- 训练并行优化：通过改造注意力掩码和位置索引，实现序列所有位置的隐态能量引导并行计算，大幅降低预训练开销

### 关键实验
预训练用Fineweb、Climbmix、DCLM三大公开语料，评测覆盖26个下游跨域任务，对比同参数量、同训练数据的GPT、MDLM基线：相同效果下比GPT少用1B~2.24B预训练token；19个零样本QA任务平均准确率超同规模GPT4.2个百分点；7个零样本生成任务平均BPB比GPT低0.02、比MDLM低0.09。

**最值得记住的一句话**：能量基模型只要打通能量引导与生成的架构壁垒，就能在预训练效率、零样本泛化上全面超越同规模自回归GPT，是下一代通用基础模型的重要候选方向。
