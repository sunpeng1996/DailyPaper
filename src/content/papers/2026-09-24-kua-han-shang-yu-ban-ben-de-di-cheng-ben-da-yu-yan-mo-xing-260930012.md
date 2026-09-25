---
title: Low-Cost Assays for Measuring Model Behavior Across Vendors and Releases
title_zh: 跨厂商与版本的低成本大语言模型行为检测方法
authors:
- Tapan Parikh
affiliations:
- Cornell Tech
arxiv_id: '2609.30012'
url: https://arxiv.org/abs/2609.30012
pdf_url: https://arxiv.org/pdf/2609.30012
published: '2026-09-24'
collected: '2026-09-25'
category: Eval
direction: LLM行为评测 · 低成本可复现检测
tags:
- LLM Evaluation
- Model Behavior
- Low-Cost Assay
- Cross-Vendor Testing
- Release Tracking
one_liner: 提出单模型成本不足几美元的可复现LLM行为检测框架，覆盖3种结果判读范式
practical_value: '- 可复用3种结果判读范式做业务LLM选型评测：简单匹配用精确匹配，需要语义判断用对齐人类标注的LLM评委，Agent行为评测用带埋点的运行环境，能大幅降低评测成本

  - 选型LLM服务时可套用该框架做跨厂商、跨版本的行为一致性校验，避免新版本上线后推荐/Agent话术、行为突变影响业务效果

  - 针对电商Agent的合规性、一致性检测，可复用「固定公开测试用例+批量执行」的思路，实现版本迭代前的快速回归校验'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM评测多聚焦能力、对抗攻击检测，缺乏可复现、低成本的日常行为跨厂商、跨版本对比方案，非结构化输出难量化统计，无法支撑持续行为追踪。
### 方法关键点
1. 测试用例固定公开，跨厂商模型统一执行，单模型测试成本≤几美元；
2. 按行为解释难度提供3种结果判读方式：限幅回复精确匹配、对齐人类标注的LLM评委基于编码表判读、埋点环境独立记录Agent实际行为。
### 关键结果数字
覆盖4年前沿闭源、开源模型版本测试发现：44个模型中27个在4次随机选词测试中至少输出1次serendipity；句尾加「right?」可让模型赞同度最高波动32个百分点，模型迭代后会从谄媚转向拒绝；模型承压时的立场坚持度与代际相关，坚持方式与训练厂商强相关。
