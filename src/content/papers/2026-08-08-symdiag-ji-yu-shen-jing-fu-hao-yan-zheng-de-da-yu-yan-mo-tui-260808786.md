---
title: 'SymDiag: Explainable Diagnosis for LLM Reasoning via Neuro-Symbolic Verification'
title_zh: SymDiag：基于神经符号验证的大语言模型推理可解释诊断框架
authors:
- Wenyao Cui
- Huaping Zhang
- Yongyi Huang
- Qiuchi Li
- Jian Xu
- Cheng-Lin Liu
- Chunxiao Gao
- Juan Wang
- Baohua Zhang
affiliations:
- Beijing Institute of Technology
- Zhongguancun Academy
- Institute of Automation, Chinese Academy of Sciences
- Xinjiang Future Enterprise Incubator Co., Ltd.
arxiv_id: '2608.08786'
url: https://arxiv.org/abs/2608.08786
pdf_url: https://arxiv.org/pdf/2608.08786
published: '2026-08-08'
collected: '2026-08-11'
category: Reasoning
direction: LLM可信推理 · 神经符号诊断
tags:
- LLM
- Chain-of-Thought
- Neuro-symbolic
- Reasoning
- Explainability
one_liner: 提出神经符号诊断框架SymDiag，定位LLM推理故障，区分翻译与推理错误，输出可验证证据指导修复
practical_value: '- 电商导购/营销Agent的CoT质检可复用双分支符号转换+自审计设计，区分表述歧义和真实逻辑错误，避免误判推理质量，降低优惠计算、规则匹配类客诉

  - 大模型自我修复模块可参考故障定位+证据反馈的闭环设计，仅修改错误步骤而非全链路重生成，降低推理延迟和算力成本

  - 高可靠场景的推理校验可复用步骤级符号验证思路，输出反例、缺失前提等可审计证据，满足合规性要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM的CoT推理常存在「答案正确但步骤不忠实」的问题，传统验证方案存在明显缺陷：仅匹配最终答案无法定位故障，LLM-as-judge输出主观不可审计，PRM仅输出标量分数无解释性；同时神经符号方法普遍无法区分翻译噪声与真实推理缺陷，易出现误诊断，阻碍LLM在高可靠场景落地。
### 方法关键点
1. 两阶段架构：第一阶段完成推理故障诊断，第二阶段基于诊断结果做精准修复
2. 双分支符号编译：将CoT分别转换为形式化翻译、批判性重述两个独立的Prolog程序，降低单路径翻译偏差
3. 自审计模块：通过双分支一致性校验+轻量逻辑检查，明确区分TranslationError与ReasoningError，避免误判
4. 步骤级符号验证：逐步做可满足性、蕴含性检查，定位故障点并输出反例、不一致见证、缺失前提等可验证证据
5. 差异化修复：根据故障范围选择局部补丁（仅改错误步骤）或全局重写（从故障点重推）
### 关键结果
在覆盖数学、逻辑、科学、通用推理的240条人工标注CoT数据集上，对比4类基线：
- 推理忠实度检测F1达70.7，比第二名LogicReward高3.8个百分点
- 4轮修复后所有数据集精度提升幅度均显著超过基线，小模型修复收益更突出
### 核心结论
SymDiag不是更好的验证器或奖励函数，而是一套可解释的神经符号诊断系统，能跨领域定位、归因、修复推理故障并提供可验证的证据
