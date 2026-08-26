---
title: 'Beyond What Meets the Eye: Unveiling Situational Illusions for Multimodal
  Large Language Models'
title_zh: 眼见未必为实：多模态大模型情境错觉问题研究
authors:
- Zhiming Yang
- Zhuoxi Xiong
- Donglin Zhou
- Wenjun Wei
- Shiyao Cui
- Jinqiao Shi
affiliations:
- 北京邮电大学
- 北京邮电大学人工智能学院
arxiv_id: '2608.22232'
url: https://arxiv.org/abs/2608.22232
pdf_url: https://arxiv.org/pdf/2608.22232
published: '2026-08-23'
collected: '2026-08-26'
category: Multimodal
direction: 多模态大模型 · 鲁棒性评测与优化
tags:
- MLLM
- Situational Illusion
- Benchmark
- Robustness
- Prompt Engineering
- SFT
one_liner: 提出多模态大模型情境错觉分类体系与MSIBench评测基准，配套两种优化方案最高提效20%
practical_value: '- 电商多模态商品理解、直播内容审核场景可引入情境错觉校验逻辑，避免因包装、拍摄角度等误导产生识别错误，比如把装牛奶的视觉倒置款杯子误判为真倒置

  - 闭源MLLM落地多模态业务时，可复用「系统核查视觉证据+上下文关联推理」的prompt模板，无需微调即可提升复杂场景识别准确率，最高增益达20%

  - 开源MLLM适配实景场景时，可基于开源MSIBench数据集做SFT，低成本提升多模态感知鲁棒性，适配实体Agent、线下导购等复杂交互需求'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现实场景中视觉表象常与真实物理状态存在偏差（即情境错觉），会导致MLLM在实体Agent、内容理解、实景交互等落地场景出现决策错误，当前缺乏对该问题的系统性评测与优化方案。
### 方法关键点
1. 构建where-what-how三维分类体系，明确情境错觉的发生位置、作用目标、产生机制；
2. 发布MSIBench评测基准，覆盖MLLM的判别、理解、推理三类核心能力的鲁棒性评估；
3. 针对闭源模型设计引导系统核查视觉证据的prompt方案，针对开源模型基于基准数据做SFT优化。
### 关键结果
对27种MLLM配置评测发现，现有模型普遍易受情境错觉干扰，存在6类与视觉观察、grounding、推理相关的典型失效模式；两种优化方案最多可提升模型性能20%。
