---
title: 'FreqForcing: Autoregressive Long Video Generation via Spectral Self-Anchoring'
title_zh: FreqForcing：基于频谱自锚定的自回归长视频生成方法
authors:
- Jiatong Li
- Leo Liang
- Linghe Kong
- Yulun Zhang
affiliations:
- Shanghai Jiao Tong University
- Tencent HY Team
arxiv_id: '2607.27110'
url: https://arxiv.org/abs/2607.27110
pdf_url: https://arxiv.org/pdf/2607.27110
published: '2026-07-29'
collected: '2026-07-31'
category: Other
direction: 自回归长视频生成 · 频谱锚定优化
tags:
- Video Generation
- Autoregressive Model
- Frequency Domain
- Training-free
- Diffusion Model
one_liner: 提出训练无关的FreqForcing框架，通过频谱自锚定解决自回归长视频生成的长序列误差累积
practical_value: '- 电商长序列生成场景（如商品展示长视频、虚拟直播连续画面生成）的误差漂移问题，可借鉴高低频拆分思路：低频分量保整体风格/色彩一致性，高频分量保动态细节

  - 算力有限无法重训大模型的场景，可参考该无训练优化框架的设计思路，仅通过推理侧改造提升长序列生成效果

  - Agent生成长时序交互内容（如虚拟导购连续对话+画面输出）时，可借鉴锚定+局部注意力拆分的思路，维持整体信息一致性的同时保留交互动态性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
自回归视频扩散模型支持实时流视频生成，但自推理阶段的误差会随序列长度累积，最终出现色彩漂移、运动停滞甚至视觉崩溃；现有attention sink方案仅能部分缓解频域能量漂移，无法彻底解决该问题。
### 方法关键点
从频域视角定位误差累积的本质是低频频段能量漂移，提出训练无关的FreqForcing框架，核心为频谱自锚定（SSA）机制：复用锚定注意力的低频分量维持长时序视觉稳定性，保留局部注意力的高频分量保证动态运动细节。
### 关键结果
将仅在5秒视频片段上预训练的Self-Forcing模型扩展到支持2分钟视频生成，实现24倍长度外推；效果在定量、定性指标上均优于现有无训练方法，与主流有训练方案表现持平。
