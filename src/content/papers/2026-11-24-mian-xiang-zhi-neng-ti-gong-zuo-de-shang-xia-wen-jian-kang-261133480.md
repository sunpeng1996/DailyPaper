---
title: 'DevEx is for Humans, AX is for Agents: Measuring Context Health in Agentic
  Software Work'
title_zh: 面向智能体工作的上下文健康度评估框架AX及其实证验证
authors:
- Gratiana Fu
- Josh Beitler
- Brian Houck
affiliations:
- DX, Salt Lake City, USA
arxiv_id: '2611.33480'
url: https://arxiv.org/abs/2611.33480
pdf_url: https://arxiv.org/pdf/2611.33480
published: '2026-11-24'
collected: '2026-11-26'
category: Agent
direction: 智能体上下文质量评估 · Agent Experience
tags:
- Agent Experience
- Context Quality
- CAFE Framework
- LLM-as-Judge
- Agent Evaluation
one_liner: 提出基于CAFE四维度的AX评估框架，可自动衡量智能体执行任务时的上下文健康质量
practical_value: '- 搭建业务Agent（如推荐决策Agent、客服Agent）时，可复用CAFE四维度（Clarity/Actionability/Fidelity/Efficiency）设计上下文质检流程，替代仅看任务成功率的粗放评估，快速定位上下文缺陷根因

  - 用LLM-as-Judge做评估时，可参考本文的分维度锚定打分规则+证据要求设计prompt，优先选择能力更强的大模型作为评估器，本文中GPT-6系列对目标上下文缺陷的检出率可达85%，是Claude
  Haiku 4.5的1.7倍

  - 电商/推荐场景的Agent任务中，上下文缺陷往往先体现在token消耗上涨而非效果下降，可将AX评分、token消耗涨幅组合成预告警指标，提前发现问题降低推理成本'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前智能体评估多仅关注输出结果，无法定位执行过程中上下文相关阻碍；工业界AI投入持续上涨但效率提升不及预期，上下文质量是核心影响因素之一，亟需可落地的上下文健康度度量工具。
### 方法关键点
- 借鉴开发者体验（DevEx）思路提出Agent Experience（AX）评估框架，基于CAFE四维度（Clarity清晰度、Actionability可执行性、Fidelity保真度、Efficiency效率）设计1-5分rubric打分规则，要求评估必须给出对应证据支撑
- 采用LLM-as-Judge实现自动化评估，可直接对Agent会话转录文本打分并给出可落地的上下文优化建议
- 三类实验交叉验证：Stack Overflow 2026开发者调研二次分析、1000条自然Agent会话的量表稳定性验证、注入上下文缺陷的可控场景测试
### 关键结果数字
- 调研显示遇到上下文问题的开发者认为AI「非常有用」的比例低12%-28%
- 882条有效自然会话中Actionability维度评分最低，59.6%的评分≤3；Fidelity维度评分最高，仅26.6%≤3
- 可控场景中所有注入缺陷的任务token消耗平均上涨91%，5款评估模型对目标缺陷的检出率为50%-85%，Fidelity缺陷检出最稳定，Actionability缺陷最难检出

**最值得记住的一句话**：智能体任务中上下文缺陷往往先体现为推理成本上涨，而非直接的输出错误，上下文质量优化是降本提效的核心抓手
