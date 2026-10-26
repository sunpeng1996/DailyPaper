---
title: Do "True" and "False" Add Up to One? Complement Consistency in LLM-Agent Opinion
  Simulations
title_zh: LLM-Agent观点模拟的补集一致性校验：真假概率之和是否为1
authors:
- Anouar Imel
- Jin Qi
affiliations:
- University of Electronic Science and Technology of China (UESTC)
arxiv_id: '2610.32874'
url: https://arxiv.org/abs/2610.32874
pdf_url: https://arxiv.org/pdf/2610.32874
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: LLM Agent 观点模拟一致性评估
tags:
- LLM-Agent
- Opinion Simulation
- Consistency Check
- Probability Elicitation
- Repair Method
one_liner: 验证3款小开源LLM Agent观点模拟不满足补集一致性，提出对称修复方案
practical_value: '- 做基于Agent的用户舆情模拟、消费决策仿真、广告效果推演时，必须先做补集一致性校验，避免表述措辞差异导致仿真结果完全不可信

  - 对需要LLM输出概率的业务场景（如广告合规度打分、商品匹配度辅助判断），可直接复用对称修复trick：同时查询原命题和补集命题，取`(q0 + 1 - q1)/2`作为最终概率，天然保证逻辑一致性，降低平均Brier
  loss

  - 设计Agent仿真实验时，不要仅验证干预策略的效果稳定性，需单独测试本地更新的表述鲁棒性，否则结论可能是措辞带来的伪影'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM Agent被广泛用于观点动力学、舆情仿真、群体决策模拟等场景，其输出的概率会作为后续迭代的状态输入，但如果同一个事实的正反表述会导致输出概率不满足和为1的基本逻辑约束，会直接导致仿真轨迹失真，过往研究缺少对这类一致性的系统校验。

### 方法关键点
- 定义补集一致性校验规则：将命题`c`、初始概率`p`、邻居概率列表`r`替换为补集命题`¬c`、`1-p`、`1-r`，LLM输出的两个概率之和应等于1，差值`δ`为不一致度
- 测试3款主流小开源模型：Qwen3-4B、Llama-3.2-3B、Gemma-3-4B
- 覆盖三类测试场景：仿真运行中抽取的2304个Agent状态、48条AVeriTeC真实事实核查claim、24个严格二分类的控制基准世界
- 验证无偏修复方案：对称化处理，取`R=(q0 + 1 - q1)/2`作为修正后的概率，天然满足补集一致性

### 关键结果数字
- 三类场景下所有模型均出现一致性失效：Qwen在仿真状态集上平均`δ=0.18`，真实claim集上平均绝对`δ=0.33`
- 不一致度是同义改写敏感度的2-10倍，跨peer数量、报告强度、重复采样均稳定存在
- 补集初始状态的两个仿真群体经过5轮迭代后，所有模型的轨迹偏离度均为正
- 对称修复可100%保证逻辑一致性，平均Brier loss下降，仅Gemma修复后效果优于最优原表述基线

最值得记住的结论：将LLM生成的概率作为Agent状态用于闭环仿真前，必须同时报告补集一致性和事实准确率，否则结论可能不可靠
