---
title: 'Beyond Artifacts: Towards Generalizable Synthetic Song Detection via Music-Intrinsic
  Features'
title_zh: 超越人工痕迹：基于音乐固有特征的通用合成歌曲检测
authors:
- Yan Han
- Zhibin Wen
- Yuan Wang
- Shuangrun Shao
- Xiaobing Li
- Yang Xu
- Wei Li
affiliations:
- Central Conservatory of Music
- Southern University of Science and Technology
- Fudan University
arxiv_id: '2606.16612'
url: https://arxiv.org/abs/2606.16612
pdf_url: https://arxiv.org/pdf/2606.16612
published: '2026-06-15'
collected: '2026-06-27'
category: Other
direction: 合成歌曲检测 · 多模态特征融合
tags:
- Synthetic Detection
- MoE
- Audio Feature
- Benchmark
- Multimodal
one_liner: 提出基于音乐固有特征与自适应MoE的合成歌曲检测框架Sofia，配套开源MUSIC8K基准数据集
practical_value: '- 多模态生成内容（AI音频/视频/广告文案）检测任务可复用「分维度特征训练专属专家+自适应MoE融合」架构，相比端到端训练泛化性更强，可适配不同生成工具产出的伪造内容

  - 做AIGC检测类需求时，避免仅依赖低阶人工痕迹特征，优先挖掘内容本身的固有结构/属性特征，对抗生成工具迭代带来的检测失效问题

  - 检测类任务的benchmark构建可参考其思路：覆盖最新生成工具+加入真实场景扰动，避免离线指标虚高、线上效果差的问题'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
AI音乐生成工具大幅降低创作门槛，合成歌曲难以通过人工感知区分，给流媒体平台版权治理、原创保护带来巨大挑战；现有合成歌曲检测方法依赖低阶人工痕迹、固定特征假设，无法适配不同生成器，泛化性差。
### 方法关键点
1. 提出Sofia框架：针对人声、音频效果、全局结构三类音乐固有特征分别训练专属特征专家，再通过自适应MoE模块融合多维度特征输出检测结果
2. 构建MUSIC8K基准数据集：覆盖最新Suno、Udio等生成工具，加入真实场景音频扰动，提升测试难度
### 关键结果
在MUSIC8K-O数据集上F1值较最优基线提升18.5个点，同时具备强鲁棒性，可学习到跨生成器的通用表征。
