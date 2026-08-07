---
title: 'The Next Screenshot Knows: Gated Hindsight Distillation for Mobile GUI Agents'
title_zh: 门控后验蒸馏：利用下一帧截图优化移动GUI Agent训练
authors:
- Weiwei Li
- Junzhuo Liu
- Tong Chu
- Hengfu Yu
- Wen Li
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2608.06065'
url: https://arxiv.org/abs/2608.06065
pdf_url: https://arxiv.org/pdf/2608.06065
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: GUI Agent 离线训练优化
tags:
- GUI Agent
- Distillation
- Reinforcement Learning
- Offline Training
- Vision-Language Model
one_liner: 训练时将下一帧截图作为特权信息，通过门控后验蒸馏提升GUI Agent任务成功率
practical_value: '- 做交互式Agent（如电商导购Agent、自动化运营Agent）离线训练时，可将轨迹中后续的反馈/状态作为训练特权信息，蒸馏到仅观测历史的推理模型中，不增加推理成本即可提升效果

  - 蒸馏时增加门控逻辑，仅在学生模型预测错误、且特权信息增强的教师模型可输出正确结果时触发蒸馏，避免噪声信号干扰，提升蒸馏效率

  - 分布式训练可增加动态采样逻辑，最多重试3次采样学生输出，直到拿到符合门控条件的样本，仅增加少量训练开销即可提升监督信号密度

  - 序列决策类推荐/Agent任务优先用分布匹配的蒸馏方式，而非单样本STaR式自训练，可获得更细粒度的监督信号，效果提升更明显'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有GUI Agent离线训练仅从历史前缀预测动作，很多动作的合理性证据（如点击某菜单后才出现的目标功能）只存在于后续的下一帧截图中，导致监督信号缺失，模型难以学到可落地的推理逻辑，模仿学习和普通RL的效果瓶颈明显。

### 方法关键点
- 提出Gated Hindsight Distillation（GHD）框架，训练时设置参数共享的师生模型，学生仅观测历史前缀，教师额外获得轨迹中已有的下一帧截图作为特权信息
- 增加双条件门控：仅当学生预测错误、且教师在学生的输出前缀基础上能修正得到正确示范动作时，才执行蒸馏，过滤不可靠信号
- 训练目标为GRPO损失加λ=0.1的蒸馏损失，蒸馏用对称Jensen–Shannon散度匹配教师和学生的token分布，覆盖推理和动作输出全序列
- 增加动态采样机制，每个批次最多重试3次采样学生输出，提升有效监督样本的密度

### 关键实验结果
在AndroidWorld、AndroidLab两个移动GUI Agent基准上测试，对比SFT、GRPO baseline：7B模型AndroidWorld Pass@1从47.13提升到52.73，AndroidLab Pass@1从31.93提升到43.10；8B模型AndroidWorld Pass@1从61.35提升到66.47，AndroidLab Pass@1从37.43提升到54.11，在7个测试APP上效果优于GRPO，且推理无额外开销。

最值得记住的一句话：离线训练序列决策类Agent时，轨迹中已有的未来状态是低成本的强特权信息，通过门控蒸馏可以在不增加推理成本的前提下大幅提升模型效果。
