---
title: 'TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models'
title_zh: TempJail：针对图像转视频生成模型的时序越狱攻击
authors:
- Qi Lu
- Zehui Guo
- David Yuanda Gan
- Zijing Li
- Hengda Zhang
- Weijun Xu
- Qiankun Zhang
affiliations:
- 华中科技大学
- 北京大学
- 南京大学
arxiv_id: '2608.26971'
url: https://arxiv.org/abs/2608.26971
pdf_url: https://arxiv.org/pdf/2608.26971
published: '2026-08-27'
collected: '2026-08-29'
category: Other
direction: 生成式多模态 · 模型安全攻击
tags:
- Jailbreak Attack
- Image-to-Video Generation
- Diffusion Model
- Adversarial Attack
- Multimodal Safety
one_liner: 发现图像转视频模型时序维度安全漏洞，提出TempJail框架大幅提升黑盒越狱攻击成功率
practical_value: '- 电商带货/广告短视频生成场景的安全防护，需新增跨帧时序语义校验逻辑，不能仅依赖单帧违规检测

  - 短视频合规审核场景可参考本文时序语义组合逻辑，补充动态维度违规检测规则，降低漏审率

  - 对外提供I2V生成服务的业务可复用该攻击逻辑做红蓝对抗测试，提前挖掘并修复安全隐患'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有图像转视频（I2V）生成模型安全研究仅关注单帧违规越狱攻击，忽略了视频独有跨帧时序语义组合带来的新型安全风险，且时序攻击存在时序抽象、语义伪装两大核心难点。
### 方法关键点
提出TempJail时序越狱框架：1. 时序抽象层：将恶意目标描述拆解为初始帧视觉条件+时序文本指令的分层结构；2. 双模态语义伪装：图像侧在扩散采样latent空间添加预训练编码器梯度引导的可控扰动注入语义，文本侧将恶意提示改写为无风险的「主体-动作-场景」模板绕过安全过滤，黑盒推理时双模态联动随时间逐步触发恶意语义。
### 关键结果
在可灵、Seedance、Veo、PixVerse等闭源商用I2V模型上测试，TempJail相比SOTA方法攻击成功率在GPT-5.2评估下提升23.3%，人工评估下提升22.0%
