---
title: 'SIRIS: Can LLMs Tell When Simulation Errors Matter in AI-Driven Systems Research'
title_zh: SIRIS：LLM能否判断AI驱动系统研究中仿真错误的实际影响
authors:
- Jinwoo Hwang
- Sukmin Cho
- Tao Zhang
- Soheil Abbasloo
- Jongse Park
- Peng Cheng
affiliations:
- KAIST
- Microsoft Research Asia
arxiv_id: '2611.10329'
url: https://arxiv.org/abs/2611.10329
pdf_url: https://arxiv.org/pdf/2611.10329
published: '2026-11-05'
collected: '2026-11-10'
category: Eval
direction: LLM系统理解能力评估 · 仿真误差场景
tags:
- LLM Evaluation
- Simulation Error
- AI-Driven Research
- System Design
- LLM Agent
one_liner: 提出SIRIS评估框架，测试LLM在仿真存在缺陷时能否正确判断系统设计推荐的有效性
practical_value: '- 做LLM Agent辅助推荐引擎调度、广告投放策略仿真优化时，不能默认LLM能正确判断仿真缺陷的影响，需额外增加仿真结果校验环节，避免错误抛弃有效策略

  - 给Agent增加self-correction轮次时要权衡收益风险：自校正能恢复部分正确决策，但也会引入新错误，业务中可先小流量测试自校正的准确率变化再全量上线

  - 若业务用仿真工具验证推荐/广告新策略，可复用SIRIS的扰动构造思路，生成多组对照workload测试LLM的决策鲁棒性，降低仿真偏差带来的策略损失'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM Agent广泛参与AI驱动的系统研究与优化流程，依赖仿真器完成大规模候选方案评估，但仿真器天然存在建模局限性，可能扭曲预测结果，缺乏方法判断LLM能否区分仿真误差是否会导致推荐方案失效。
### 方法关键点
提出SIRIS评估框架，通过对仿真器施加扰动，构造候选方案、仿真局限性、初始推荐完全一致的成对workload，仅调整扰动使得仅其中一组的初始推荐能被参考仿真器验证有效，以此测试LLM的系统理解与决策正确性。
### 关键结果
在13款前沿LLM的LLM服务设计问题测试中，发现LLM识别出仿真局限性不代表能做出正确决策，即使是SOTA模型也会错误抛弃有效推荐；增加一轮自校正review环节可恢复大量正确决策，但也会在约20%的场景下引入新错误
