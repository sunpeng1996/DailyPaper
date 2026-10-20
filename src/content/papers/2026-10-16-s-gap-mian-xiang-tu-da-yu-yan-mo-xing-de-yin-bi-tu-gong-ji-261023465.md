---
title: 'S-GAP: Stealthy Graph Attack Primitives for Graph Large Language Models'
title_zh: S-GAP：面向图大语言模型的隐蔽图攻击原语
authors:
- Wenda Li
- Tongya Zheng
- Shunyu Liu
- Hanyang Yuan
- Kaixuan Chen
- Yu Wang
- Yuchen Ying
- Haoze Jiang
- Huan Li
- Gang Chen
affiliations:
- Zhejiang University
- Hangzhou City University
- Nanyang Technological University
- Zhejiang Lab
arxiv_id: '2610.23465'
url: https://arxiv.org/abs/2610.23465
pdf_url: https://arxiv.org/pdf/2610.23465
published: '2026-10-16'
collected: '2026-10-20'
category: LLM
direction: GraphLLM 对抗攻击 · 多Agent优化
tags:
- GraphLLM
- Adversarial Attack
- Multi-Agent
- Text-Attributed Graph
- Stealth Attack
one_liner: 提出统一文本与结构扰动的GAP语义表示及多Agent迭代的S-GAP框架，提升GraphLLM攻击成功率与隐蔽性
practical_value: '- 电商商品关联网络（属于TAG）的GraphLLM应用可参考GAP统一文本+结构扰动的思路做鲁棒性测试，提前发现关联推荐、商品排序链路的漏洞

  - 多Agent迭代优化+替代评估+文本反馈的闭环框架可复用在推荐文案生成、商品关联规则挖掘等任务，提升输出内容的合理性与一致性

  - 做GraphLLM防御时可针对GAP的语义一致性特征设计扰动检测规则，降低恶意攻击对推荐效果的负面影响'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有GraphLLM对抗攻击将文本、结构扰动分阶段生成，存在攻击意图碎片化问题，扰动语义不一致导致隐蔽性差、易被模型识别过滤，最终攻击有效性低。
### 方法关键点
1. 原子语义表示GAP（Graph Attack Primitive）将文本与结构扰动统一到同一攻击意图下，通过校准语义组成平衡攻击效果与隐蔽性；
2. 多Agent框架S-GAP统一GAP的规划与生成流程，通过替代模型评估、文本反馈迭代优化扰动语义。
### 关键结果
在4个数据集、3款GraphLLM、2种攻击设置下验证，S-GAP相比最优基线攻击成功率（ASR）平均提升7.02%，生成的扰动关联合理性更高，暴露了当前GraphLLM的关键安全漏洞。
