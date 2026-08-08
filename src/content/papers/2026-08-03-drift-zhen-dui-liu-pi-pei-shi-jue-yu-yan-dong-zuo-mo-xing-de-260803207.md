---
title: 'DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial
  Patch Attack'
title_zh: DRIFT：针对流匹配视觉语言动作模型的去噪轨迹对抗补丁攻击
authors:
- Hoseong Tae
- Jong-Seok Lee
affiliations:
- Yonsei University
arxiv_id: '2608.03207'
url: https://arxiv.org/abs/2608.03207
pdf_url: https://arxiv.org/pdf/2608.03207
published: '2026-08-03'
collected: '2026-08-08'
category: Multimodal
direction: 多模态VLA · 对抗攻击方法优化
tags:
- Adversarial Attack
- Flow Matching
- Vision-Language-Action
- Universal Adversarial Patch
- VLA Robustness
one_liner: 提出仅攻击流匹配VLA首步去噪过程的通用对抗补丁 击穿其宣称的高鲁棒性
practical_value: '- 生成式推荐/多模态文案生成场景使用流匹配类模型时，可复用「仅攻击首步去噪过程」的思路做鲁棒性校验，测试成本远低于全链路攻击方案

  - 通用对抗补丁的设计逻辑可迁移到多模态商品内容的隐形水印植入、AI生成内容溯源场景，实现低侵入性的内容标识与版权校验

  - 多模态决策Agent部署安全评估可参考该结论：流匹配类生成模型的宣称鲁棒性存在显著漏洞，不可直接用于高安全要求的决策链路'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
流匹配VLA（如pi0）此前被宣称对对抗扰动具备高鲁棒性，远优于自回归VLA，但该鲁棒性本质未得到深入验证，模型落地安全评估存在显著盲区。
### 方法关键点
提出DRIFT测试时通用对抗补丁，可部署在机器人夹爪上直接攻击现成流匹配策略的去噪速度场；核心发现与训练时后门注入逻辑完全相反：仅攻击去噪ODE的第一步，即可利用输入空间优化独有的梯度冲突特性，实现比多步攻击更强的效果、更低的计算成本。
### 关键结果
在pi0、pi0.5两款模型的4个LIBERO测试集上，单个小尺寸补丁即可击穿几乎所有原本可完成的任务，性能远超动作空间、嵌入空间的基线攻击方案。
