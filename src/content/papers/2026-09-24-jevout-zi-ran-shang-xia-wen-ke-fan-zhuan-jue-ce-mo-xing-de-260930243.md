---
title: 'JevOut: Natural Context Can Flip Decision Models'
title_zh: 《JevOut：自然上下文可反转决策模型的输出结果》
authors:
- Zixiang Xu
affiliations:
- University of Southern California
arxiv_id: '2609.30243'
url: https://arxiv.org/abs/2609.30243
pdf_url: https://arxiv.org/pdf/2609.30243
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: Agent决策模型鲁棒性安全分析
tags:
- Robustness
- Decision Model
- Agent Safety
- Adversarial Test
- LLM
one_liner: 验证短自然上下文可高概率反转专用决策模型的正确输出，暴露其严重鲁棒性缺陷
practical_value: '- 部署电商客服Agent、推荐请求路由模块时，必须加入上下文扰动鲁棒性校验，避免会话冗余信息干扰意图/路由决策

  - 对于直接用概率阈值触发下游动作的决策模型，需额外增加输入上下文的无关性过滤逻辑，降低噪声对广告投放、商品推荐决策的影响

  - 上线前可复用论文的梯度引导上下文生成方法，对决策模块做白盒对抗测试，提前发现鲁棒性漏洞，减少线上故障'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前Jev等专用决策模型可直接将自然语言映射为有限选项的概率分布，被广泛用于Agent工具选择、请求路由、动作触发等场景，但实际输入往往附带大量背景上下文，这类模型的上下文鲁棒性尚未得到系统验证。
### 方法关键点
固定测试样本的原输入、问题、候选选项、金标答案，针对预设的错误目标选项，基于模型输出的选项概率迭代优化生成流畅自然的上下文附加内容，不改动原决策的核心信息。
### 关键结果
1. 针对Jev模型的508个原本正确的决策样本，61.4%（312个）可被生成的短上下文反转，其中229个案例中模型给错误选项的概率≥0.7；
2. 跨7个数据集、3类其他决策系统的测试中，原本正确的决策被定向反转的比例达64.9%~73.2%，证明该鲁棒性缺陷具备普遍性。
