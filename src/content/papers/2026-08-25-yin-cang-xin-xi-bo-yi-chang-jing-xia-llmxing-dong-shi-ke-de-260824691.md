---
title: 'Confident at the moment of action: belief miscalibration in LLM play under
  hidden information'
title_zh: 隐藏信息博弈场景下LLM行动时刻的信念校准偏差研究
authors:
- Bhushan Kashinath Joshi
arxiv_id: '2608.24691'
url: https://arxiv.org/abs/2608.24691
pdf_url: https://arxiv.org/pdf/2608.24691
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: LLM Agent 信念校准评估
tags:
- Agent
- LLM Calibration
- Belief Alignment
- Game-based Evaluation
- Hidden Information
one_liner: 通过定制国际象棋博弈实验，验证LLM高置信度行动存在严重校准偏差，常规评估无法检出
practical_value: '- 业务中若基于LLM自报告置信度设置自动执行阈值（比如电商客服自动回复、个性化推荐自动干预），不能直接采信LLM输出的置信度，需额外开发独立的置信度校验模块，尤其是涉及用户隐性需求等隐藏信息的场景

  - 评估Agent效果时，不能只看最终业务指标（点击率、解决率），要单独评估「状态推断信念」和「最终行动」的对齐度、信念校准度，避免选中“结果正确但推理完全错误”的劣化模型

  - 多轮交互场景的Agent性能测试不能用静态单轮评估代替，静态测试会显著高估模型在实际动态交互中的信念准确率，评估结果偏差可达20~40个百分点'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前越来越多Agent系统将LLM自报告的置信度作为自动行动的决策依据，默认置信度与行动正确性强相关，但该假设在存在隐藏信息的动态交互场景下从未被直接验证。常规评估范式要么仅测输出的置信度校准，要么仅测最终任务结果，无法发现“信念表述与实际行动脱节”的核心问题。
### 方法关键点
- 定制Regent Chess国际象棋变体：允许玩家秘密反复转移棋子的王室身份，隐藏状态全程后台可回溯，无观测偏差
- 每轮同时独立采集两个输出：LLM的行动（走棋）、对对手隐藏王室棋子的概率分布，避免两者互相干扰
- 采用固定规则的确定性对手，排除对手策略波动的干扰，所有对比结果可比
### 关键实验结果
- 主力测试模型Gemini 3.1 Flash-Lite的高置信度（≥0.5）吃子行动，62次中仅1次正确，准确率仅1.6%，99%以上的校准偏差集中在高置信度行动场景
- 同一款模型仅提升推理token预算（从4096到16384），校准准确率提升10.8个百分点，提升幅度与跨大模型的能力差距相当
- 某模型关闭推理模式后，在合法率、响应速度、推理成本等常规指标上全部最优，但信念准确率仅3.8%，常规评估完全无法检出该问题

仅基于最终结果、延迟、成本等常规指标的Agent评估，不仅无法发现信念校准偏差，甚至会主动筛选出信念追踪能力最差的配置。
