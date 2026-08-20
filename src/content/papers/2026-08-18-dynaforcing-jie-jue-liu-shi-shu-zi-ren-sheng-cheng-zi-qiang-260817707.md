---
title: 'DynaForcing: Overcoming Dynamic Collapse in Self-Forcing Distillation for
  Streaming Avatar Generation'
title_zh: DynaForcing：解决流式数字人生成自强迫蒸馏的动态坍缩问题
authors:
- Yubo Huang
- Sirui Zhao
- Xinchen Yao
- Zhengye Zhang
- Jinyang Huang
- Fengqi Cui
- Shiwei Wu
- Enhong Chen
affiliations:
- University of Science and Technology of China
- Nanjing University
- Hefei University of Technology
- Tsinghua University
arxiv_id: '2608.17707'
url: https://arxiv.org/abs/2608.17707
pdf_url: https://arxiv.org/pdf/2608.17707
published: '2026-08-18'
collected: '2026-08-20'
category: Multimodal
direction: 多模态生成 · 流式数字人蒸馏优化
tags:
- Audio-driven Avatar
- Knowledge Distillation
- Dynamic Collapse
- Streaming Generation
- Diffusion Distillation
one_liner: 提出DynaForcing训练框架解决流式音频驱动数字人自强迫蒸馏的动态坍缩问题
practical_value: '- 电商直播带货数字人场景可直接复用DynaForcing三层优化策略，解决自强迫蒸馏生成的数字人表情僵硬、口型不同步问题

  - 自强迫蒸馏训练时可复用计算图剪枝+梯度重放技巧，显存占用降低超10倍，大幅降低大模型蒸馏的训练成本

  - 生成类任务（如商品文案/营销素材生成）遇到静态/模式坍缩时，可参考「真值锚定+显式多样性奖励」思路修正损失与数据流程'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
流式音频驱动数字人生成采用DMD自强迫蒸馏实现实时推理，但存在动态坍缩问题：学生模型输出感知质量高但时序动态被严重抑制，口型表情同步失效，根因为反向KL目标偏向低运动模态、无锚定自条件形成反馈环放大坍缩。
### 方法关键点
从三层设计优化：数据层混合强迫锚定真值动态打破反馈环；损失层引入动态感知奖励正则化抵消反向KL偏差；条件层参考图像扰动解耦身份与静态细节，强制模型依赖音频生成运动；新增计算图剪枝+梯度重放，显存占用降低1个数量级以上。
### 关键结果
动态程度Dyn-Deg从0.31提升至0.73（接近教师模型水平），口型同步得分Sync-C从7.03提升至7.68，同时提升视觉质量，无需早停即可解决质量-动态权衡问题，推理帧率达45.2FPS满足实时要求。
