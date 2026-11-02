---
title: 'SecPO: Principled Adversarial Training for Prompt Injection Security'
title_zh: SecPO：面向提示注入安全的有原则对抗训练方法
authors:
- Sizhe Chen
- Yibo Peng
- Jaewon Chang
- Chawin Sitawarin
- David Wagner
affiliations:
- UC Berkeley
- Anthropic
- Google DeepMind
arxiv_id: '2610.41998'
url: https://arxiv.org/abs/2610.41998
pdf_url: https://arxiv.org/pdf/2610.41998
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: LLM安全训练 · 提示注入防御
tags:
- Prompt Injection
- Adversarial Training
- Preference Optimization
- DPO
- LLM Security
- Agent Security
one_liner: 提出SecPO损失与高效对抗训练pipeline，大幅降低提示注入攻击成功率且无明显效用损失
practical_value: '- 业务Agent处理第三方商品评论、爬虫页面、用户UGC等非信任输入时，可直接用SecPO替换DPO做偏好优化，锚定干净输入下的模型输出分布，既能提升抗提示注入能力，又不会损失正常任务的推理效果

  - 论文开源的强对抗攻击样本数据集可直接复用，无需自行生成昂贵的在线攻击样本，大幅降低电商大模型Agent安全微调的成本，适配快速迭代需求

  - 多模态Agent无需单独做视觉提示注入专项训练，文本注入的微调效果可直接迁移到多模态场景，进一步降本增效

  - 训练得到的安全模型兼容8bit量化、投机解码等常见推理优化手段，无需额外重训即可直接上线高吞吐的生产环境'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前SOTA提示注入防御方案Meta-SecAlign基于DPO训练，锚定不安全的原始参考模型，且仅在弱模拟攻击样本上训练，自适应攻击下攻击成功率（ASR）接近100%，严重阻碍AI Agent落地，尤其是电商场景下Agent处理商品评论、第三方页面、用户UGC等非信任输入时极易被攻击者劫持造成损失。
### 方法关键点
- 提出SecPO损失，替换DPO中的原始参考模型为理想注入不变神谕，神谕的输出分布可通过原始模型在干净输入上的输出直接获取，仅需对DPO损失做极小修改即可实现
- 设计高效对抗训练pipeline，基于高并发搜索式攻击PAIR生成强注入样本（best@240），支持离线复用生成的攻击数据集，大幅降低训练成本
- 梯度层面自动放大注入敏感样本的权重，优先优化高风险样本的防御效果
### 关键实验结果
在LLaMA3.1-8B、Qwen3.6-27B上验证，对比Meta-SecAlign：对抗训练使三类SOTA自适应攻击的ASR降低1.5~14.5倍，SecPO损失在对抗训练基础上进一步降低ASR 2.4~4.6倍；SecPO+AT训练的Qwen3.6-27B在AgentDojo的AttackerMovesSecond攻击下ASR仅8.8%（Meta-SecAlign为78.8%），在9项涵盖工具调用、指令跟随、科学、数学的基准上无明显效用下降，且无需专项训练即可抵御视觉提示注入（ASR 0%）。
### 核心结论
提示注入防御不需要牺牲模型效用，通过锚定干净输入分布的偏好优化+强攻击样本训练，即可实现安全与效用的平衡。
