---
title: When Does Supervised Fine-Tuning Reduce Instruction Sensitivity?
title_zh: 监督微调降低指令敏感度的适用边界与影响因素研究
authors:
- Jaekeol Choi
affiliations:
- Hankuk University of Foreign Studies
arxiv_id: '2608.26661'
url: https://arxiv.org/abs/2608.26661
pdf_url: https://arxiv.org/pdf/2608.26661
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: LLM SFT 指令敏感度影响因素研究
tags:
- SFT
- instruction sensitivity
- prompt robustness
- LLM evaluation
- LoRA
one_liner: 揭示SFT降低指令敏感度的规模依赖规律、训练指令异质性及评估协议偏差
practical_value: '- 业务上用1.7B-4B小模型做单指令SFT即可天然降低54%-71%的指令敏感度，无需额外做prompt augmentation，可降低训练成本

  - 7B及以上大模型SFT的指令鲁棒性受训练指令选择影响大，上线前必须做多 paraphrase 指令的鲁棒性测试，避免单指令评估高估真实效果

  - 评估电商相关性判断、Query理解等任务时，优先采用forced-choice（标签似然比对）评估方式，相比free generation结果更稳定，可降低评估导致的敏感度虚高

  - 大模型SFT若要追求低指令敏感度，可优先选择简洁的短训练指令，相比带详细规则的长指令，更大概率获得更稳定的跨指令性能'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM对同任务不同表述的指令存在明显性能波动，直接影响搜索推荐场景下相关性判断、重排序等任务的部署稳定性；现有研究多关注加入指令多样性的训练方案，而常规固定单指令的SFT是否能天然降低指令敏感度、效果受哪些因素影响尚不明确，单指令评估也可能无法反映模型真实鲁棒性。
### 方法关键点
- 定义指令敏感度为同一模型在多组语义等价的paraphrase指令下任务性能的标准差，ΔS为SFT前后敏感度差值，负号代表敏感度降低
- 控制实验选用同系列Qwen3 1.7B/4B/8B模型，搭配Mistral-7B、Gemma-2-9B做跨模型验证，统一用LoRA做SFT，训练仅用单条固定指令，评估用10条无重叠的语义等价指令
- 对比free generation、forced-choice两种评估协议对敏感度测量结果的影响
### 关键结果
- MS MARCO段落排序任务上，1.7B/4B Qwen3的SFT可稳定降低54%-71%的指令敏感度，不受训练指令选择影响
- 8B Qwen3单条训练指令的SFT敏感度变化不显著，但不同训练指令的敏感度差异统计显著，Gemma-2-9B呈现相同趋势，Mistral-7B无该效应
- ESCI电商相关性任务上，两种评估协议的平均准确率接近，但free generation会得出SFT后敏感度上升的结论，forced-choice则无该现象，且有效标签生成率均高于99.8%，排除格式误差影响

最值得记住的结论：SFT不会统一降低指令敏感度，其鲁棒性效果受模型规模、训练指令、模型架构共同影响，且评估协议本身会显著影响敏感度测量结果。
