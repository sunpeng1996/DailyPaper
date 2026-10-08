---
title: 'PatchBench: Measuring Collateral Damage in Activation Patching'
title_zh: PatchBench：LLM激活补丁的附带损伤评测基准
authors:
- Alexi Canesse
- Mathis Le Bail
- Maël Jenny
- Clément Elliker
- Mahammed El Sharkawy
- Sonia Vanier
affiliations:
- LIX (École Polytechnique, IP Paris, CNRS), France
- AMIAD (Agence Ministérielle pour l’IA de Défense), France
arxiv_id: '2610.10276'
url: https://arxiv.org/abs/2610.10276
pdf_url: https://arxiv.org/pdf/2610.10276
published: '2026-10-07'
collected: '2026-10-08'
category: Eval
direction: 大语言模型安全补丁效果评测
tags:
- LLM Safety
- Activation Patching
- Jailbreak Defense
- Evaluation Benchmark
- Collateral Damage
one_liner: 提出LLM激活补丁评测基准与本地协议，精准识别越狱修复的附带损伤
practical_value: '- 搭建电商/客服类LLM Agent的安全能力时，不要仅依赖全局拒答率、攻击成功率等指标，需新增局部邻域prompt测试，避免误拒正常用户的相似结构/关键词请求

  - 做LLM微调、激活补丁等优化后的效果验证时，可复用三类邻域prompt构造方法：同意图有害变体、同结构良性样本、同关键词良性样本，精准评估修复的泛化性和误伤率

  - 电商内容风控模型迭代后，可参考该评测框架，避免为拦截违规内容误伤正常的商品咨询、交易相关合法请求'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM越狱修复的评测仅依赖攻击成功率、拒绝率、全局能力得分等聚合指标，无法区分是精准修复了有害行为，还是通过局部广泛抑制误伤了大量相似的良性请求，存在严重的指标盲区。
### 方法关键点
1. 从37个公开数据集的27870条prompt出发，经过WildGuard过滤、Elo排序、人工验证，构造覆盖8个开源指令微调模型的400条高置信度越狱失败样本库。
2. 推出PatchBench-Local评测协议，对每条有害源prompt生成三类邻域样本：保留恶意意图的有害变体、结构匹配的良性prompt、复用有害关键词的良性prompt，同时评估有害变体拦截率和良性样本保留率，精准定位附带损伤。
### 关键结果
评测4种SOTA激活导向方法发现，全局MMLU得分几乎无下降的情况下，局部良性样本的误伤问题十分严重，传统全局指标会遗漏绝大部分核心附带损伤。
