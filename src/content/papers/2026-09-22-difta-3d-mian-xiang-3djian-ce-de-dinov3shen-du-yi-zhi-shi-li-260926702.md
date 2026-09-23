---
title: 'DIFTA-3D: Depth-Consistent Instance-Level Feature Transfer and Adaptation
  of DINOv3 for 3D Detection'
title_zh: DIFTA-3D：面向3D检测的DINOv3深度一致实例级特征迁移适配
authors:
- Linman Wang
- ZiFei Zhang
- Chunran Zheng
- Xiwang Dong
- Jiarong Lin
arxiv_id: '2609.26702'
url: https://arxiv.org/abs/2609.26702
pdf_url: https://arxiv.org/pdf/2609.26702
published: '2026-09-22'
collected: '2026-09-23'
category: Other
direction: 3D目标检测 · 视觉大模型跨模态迁移
tags:
- 3D Detection
- DINOv3
- Feature Transfer
- Knowledge Distillation
- RGB-D
one_liner: 将DINOv3适配到3D检测流水线，通过深度一致特征过滤+轻量蒸馏提升检测精度
practical_value: '- 大模型跨模态/跨域特征迁移时，可加入模态/域一致性校验规则过滤噪声特征，避免跨域匹配偏差，适配到推荐场景可用于多模态用户/物品表征对齐

  - 冻结基座大模型做下游任务适配时，可仅对正样本区域/正样本对做低强度蒸馏，既保留基座通用能力又降低适配计算成本，可用于LLM4Rec的微调流程

  - 离线预计算并缓存大模型生成的特征，避免推理时重复调用大模型，可显著降低推荐系统推理延迟，适合大模型落地的工程优化'
score: 6
source: arxiv-cs.CV
depth: abstract
---

# 动机
现有RGB-D 3D实例检测器依赖任务专属2D检测分支，特征提取耦合独立训练的2D检测器与图像域标签，泛化性差；直接替换为冻结视觉大模型会引入遮挡噪声、补丁特征与几何感知检测特征不匹配问题。
# 方法关键点
将DINOv3适配到IIFNet3D实例级融合流水线，核心为深度一致特征管线：将场景点投影到校准RGB-D帧，通过度量深度残差校验过滤噪声特征，将合格DINOv3特征平均存入离线点缓存，在提案对齐RoI网格内聚合缓存特征；保留几何双向实例融合路径，仅对正RoI应用低强度支持加权语义蒸馏（Conservative VAID）。
# 关键结果数字
在ScanNetV2数据集上：
- 基线DINOv3控制组在IoU 0.25/0.50阈值下mAP分别达76.15/60.93
- 加入Conservative VAID后mAP分别达76.59/62.16，较基线提升0.44/1.23个点
