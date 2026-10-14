---
title: Latent World Action Model for GUI Agents
title_zh: 面向GUI Agent的隐空间世界动作模型
authors:
- Seungjun Yu
- Hojun Choi
- Seojeong Park
- Jaeyo Shin
- Hyunjung Shim
affiliations:
- Korea Advanced Institute of Science and Technology (KAIST)
arxiv_id: '2610.14228'
url: https://arxiv.org/abs/2610.14228
pdf_url: https://arxiv.org/pdf/2610.14228
published: '2026-10-08'
collected: '2026-10-14'
category: Agent
direction: GUI Agent · 世界模型效率优化
tags:
- GUI Agent
- World Model
- Contrastive Learning
- Latent Representation
- LoRA
one_liner: 将GUI世界模型预测目标从全屏幕重建转为隐空间动作诱导信息，通过对比学习解决捷径问题，兼顾性能与推理效率
practical_value: '- 电商APP自动化导购、售后类GUI Agent可直接放弃像素级/代码级世界模型路线，改用隐空间动作后果预测方案，可在几乎不增加推理延迟的前提下提升任务成功率

  - 带未来预测的决策模型可复用「共享主干+动作头+过渡头」联合训练范式，推理时丢弃过渡头，完全避免预测模块带来的额外开销

  - 训练时遇到模型倾向于复用当前输入信息的shortcut问题，可引入动作感知对比损失，将当前状态、无关过渡状态作为负例优化，显著提升模型对动作带来的变化的建模能力

  - 现有GUI Agent的效果优化可直接基于基础Agent生成的候选动作做隐空间重排，仅需LoRA微调多模态大模型，训练成本低、迭代速度快'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有像素级GUI世界模型采用「先生成未来屏幕再重感知选动作」的两阶段范式，存在两大核心痛点：一是像素/代码级重建计算成本极高，推理延迟无法满足实时GUI交互要求；二是重建全屏幕外观的优化目标会引发identity shortcut问题——模型倾向于保留当前屏幕信息而非建模动作诱导的状态变化，尤其在GUI界面跳转差异大的场景下，反而会降低动作选择准确率。
### 方法关键点
- 基于LoRA微调多模态大模型作为共享主干，输入当前截图、任务目标、交互历史与候选动作，输出动作级共享隐表示，同时对接两个轻量头：动作头直接映射得到候选动作得分，过渡头预测对应动作的下一个状态隐表示，全程无需重建像素级屏幕
- 引入动作感知对比损失，以真实下一个状态的隐表示为正例，当前状态隐表示、内存bank中其他过渡的隐表示为负例，强制模型区分不同动作带来的状态差异，解决identity shortcut
- 训练时联合优化动作选择损失与过渡对比损失，推理时直接移除过渡头，仅需一次前向传播即可完成候选动作重排，无额外生成开销
### 关键实验
覆盖离线（AndroidControl、AITZ）、在线（AndroidWorld）、跨App OOD（GUI-Odyssey）三类场景，对比无世界模型的基础Agent、Code2World（代码级重建）、Diffusion2Image（像素级重建）两类主流世界模型：在线场景下成功率相对像素级世界模型最高提升40.6%，推理延迟最高降低98.9%；相对基础Agent成功率最高提升47.0%，仅增加不到5%的推理开销；跨App OOD场景下效果也显著优于所有baseline。
### 核心洞见
GUI世界模型不需要还原未来屏幕的外观，只需要捕捉和决策相关的动作后果即可
