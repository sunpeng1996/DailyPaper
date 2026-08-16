---
title: 'UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action
  Models'
title_zh: UniTexture：面向视觉-语言-动作模型的跨任务通用对抗纹理
authors:
- Yukun Dai
- Mingzhe Dai
- Tianshi Wang
- Fengling Li
- Jingjing Li
- Lei Zhu
affiliations:
- 同济大学
- 穆罕默德·本·扎耶德人工智能大学
- 电子科技大学
arxiv_id: '2608.13453'
url: https://arxiv.org/abs/2608.13453
pdf_url: https://arxiv.org/pdf/2608.13453
published: '2026-08-13'
collected: '2026-08-16'
category: Agent
direction: 具身Agent VLA模型对抗安全研究
tags:
- Adversarial Attack
- VLA Model
- Embodied Agent
- Universal Adversarial Texture
- Cross-Task Transfer
one_liner: 提出跨任务通用对抗纹理攻击方案，可通过单纹理触发多任务下VLA模型的动作预测偏移
practical_value: '- 多任务大模型通用对抗样本优化思路可复用：电商多模态推荐/导购Agent鲁棒性测试时，可采用跨任务联合优化方式构造对抗样本，无需单任务单独生成，大幅提升测试效率

  - 可微分渲染+梯度回传的扰动生成方法可迁移到多模态推荐攻防场景：用于构造商品图/推荐文案的对抗样本，验证推荐模型对输入扰动的抗干扰能力

  - 对抗样本跨模型跨场景迁移特性可用于批量安全验证：同架构的多模态Agent/生成式推荐模型可共享同批对抗样本做漏洞检测，降低测试成本'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
多任务VLA模型是具身Agent的核心通用策略，可支持多类指令下的操纵任务，但现有针对机器人策略的对抗攻击多针对单任务单独优化，多任务VLA的跨任务通用漏洞未被充分挖掘，易引发物理层面的不安全行为。
### 方法关键点
1. 基于可微分渲染器实现梯度回传：将VLA模型动作输出层的梯度反向传导到3D物体的表面纹理参数，实现端到端优化
2. 跨任务联合优化共享纹理：覆盖任务、指令、状态、视角的分布，用目标动作空间损失引导预测动作向攻击者指定方向偏移，无需为每个任务单独优化纹理
### 关键结果
在OpenVLA、$\pi_{0.5}$等模型的多类操纵任务上测试，攻击下平均任务成功率从90.0%降至48.4%，且无需重新优化即可实现跨套件、跨模型的攻击迁移，验证了多任务VLA存在通用跨任务漏洞。
