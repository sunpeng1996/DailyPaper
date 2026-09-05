---
title: 'FLY-EVAL++: An Evidence-Driven Evaluation Protocol for Safety-Constrained
  Flight Prediction with Large Language Models'
title_zh: FLY-EVAL++：面向大模型安全约束飞行预测的证据驱动评估协议
authors:
- Yalun Wu
- Junfeng Fang
- Jiawei Wang
- Haotian Liu
- Qijun Yang
- Minghan Yang
- Hongcheng Guo
- Zhoujun Li
- Boyang Wang
affiliations:
- National University of Singapore
- China Telecom Artificial Intelligence Technology (Beijing) Co., Ltd.
- Xiamen University
- University of Manchester
- Yunnan University
arxiv_id: '2609.04021'
url: https://arxiv.org/abs/2609.04021
pdf_url: https://arxiv.org/pdf/2609.04021
published: '2026-09-03'
collected: '2026-09-05'
category: Eval
direction: 大语言模型安全关键场景评估
tags:
- LLM
- Evaluation
- Safety Constraint
- Metric
- Multi-dimensional Scoring
one_liner: 提出安全约束下大模型飞行预测的证据驱动多维度评估协议，弥补仅用准确率的评估缺陷
practical_value: '- 电商/广告推荐等强合规场景可借鉴该框架思路，在点击率、转化率等业务指标外，新增合规性、逻辑合理性等确定性校验维度，避免数值达标但违反业务规则的问题。

  - 多步预测类Agent任务（如用户长期行为预判、多轮导购路径规划）可复用多维度打分规则，显式校验多步推演的稳定性与约束满足度。

  - 结构化输出类LLM应用（如订单话术生成、结构化用户标签输出）可引入结构化有效性校验环节，替代仅靠人工/语义匹配的评估方式。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
安全关键物理场景下的LLM评估仅依赖准确率指标存在严重缺陷：数值接近真值的预测仍可能违反操作约束、物理逻辑不一致或结构化输出不可用，现有协议无法可靠检测这类失效模式。

### 方法关键点
提出证据驱动的FLY-EVAL++评估协议，融合协议合规性、物理可行性、安全约束三类确定性校验逻辑，结合固定评分规则聚合为可解释的多维度得分；面向飞行轨迹与姿态预测任务，扩展PilotBench基准，新增历史条件依赖、多步预测两类任务。

### 关键结果
测试66款LLM发现安全合规性是模型行为最具区分度的维度：预测性能相当的模型安全得分差距超28分，常见失效模式包括物理合理预测下的安全违规、多步推演输出不稳定。
