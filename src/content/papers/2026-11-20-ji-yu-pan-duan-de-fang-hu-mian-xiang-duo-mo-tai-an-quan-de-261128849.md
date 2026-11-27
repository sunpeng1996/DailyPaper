---
title: 'Guarding with Judgment: Learning to Intervene for Multimodal Safety'
title_zh: 基于判断的防护：面向多模态安全的主动干预学习
authors:
- Jipei He
- Cheng Cheng
- Liuguo Wang
- Zihan Wen
- Changlin Yu
- Wentao Song
- Suyun Zhao
affiliations:
- Renmin University of China
arxiv_id: '2611.28849'
url: https://arxiv.org/abs/2611.28849
pdf_url: https://arxiv.org/pdf/2611.28849
published: '2026-11-20'
collected: '2026-11-27'
category: Multimodal
direction: 多模态大模型 · 安全防护优化
tags:
- Multimodal Safety
- LLM Guard
- Safety Benchmark
- Hierarchical Intervention
- SFT
one_liner: 提出四动作多模态安全防护框架JudiAct与配套基准，性能显著优于现有SOTA防护方案
practical_value: '- 电商多模态客服、导购Agent场景可复用allow/warn/review/refuse四动作分层干预逻辑，替代二元放行/拒绝机制，兼顾安全合规与用户体验

  - 安全规则落地可借鉴「证据提取→条件判定→规则匹配」三步校验架构，badcase可直接定位到具体环节，大幅降低排查成本

  - 小样本安全防护模块训练可复用单变量替换的审计反馈迭代方法，仅需少量标注即可快速优化性能，适合业务快速迭代需求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态大模型安全防护普遍采用二元放行/拒绝逻辑，要么忽视上下文风险带来安全隐患，要么直接拒绝回应用户合理需求，且判断过程无溯源依据，无法覆盖需二次校验的模糊场景。

### 方法关键点
1. 定义allow/warn/review/refuse四类分层响应动作，构建包含20126条标注的训练审计语料与JudiBench基准，每个动作关联可验证的判断证据与上下文条件
2. 提出JudiAct防护框架，分三步校验：提取输入源明确证据、判定安全响应前置条件、匹配对应安全规则；两阶段训练：第一阶段监督学习单样本判断逻辑，第二阶段通过单变量替换评审项的审计反馈迭代优化生成效果

### 关键结果
- JudiBench上较4B基线模型的请求、回答Macro-F1提升超28个百分点
- 9个公开基准测试中，生成前后两个场景的平均交付回答得分均优于SOTA防护方案，将MM-SafetyBench攻击成功率从40.78%降至25.30%
