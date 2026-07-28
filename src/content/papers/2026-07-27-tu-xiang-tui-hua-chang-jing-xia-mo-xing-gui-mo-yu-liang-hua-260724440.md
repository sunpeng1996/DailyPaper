---
title: Bigger or Cheaper? Scale and Quantization Effects on Uncertainty Signals in
  Vision-Language Models Under Image Degradation
title_zh: 图像退化场景下模型规模与量化对VLM不确定性信号的影响
authors:
- M M Asif Ferdous
affiliations:
- Independent Researcher
arxiv_id: '2607.24440'
url: https://arxiv.org/abs/2607.24440
pdf_url: https://arxiv.org/pdf/2607.24440
published: '2026-07-27'
collected: '2026-07-28'
category: Multimodal
direction: 多模态大模型 · 端侧部署选型评估
tags:
- VLM
- Quantization
- Uncertainty Estimation
- Edge Deployment
- Model Scaling
one_liner: 固定内存预算下对比三类VLM配置的两类不确定性信号，给出端侧部署选型建议
practical_value: '- 端侧部署商品图文理解、搜图类VLM/多模态Agent时，固定内存预算优先选择更大参数量的4bit量化模型，其准确率、不确定性信号质量均优于小参数量全精度模型

  - 不要依赖VLM输出的verbalized confidence作为拒识阈值，直接取生成答案token的平均概率作为内部置信度，错误识别AUROC可高出30%以上

  - 4bit量化对VLM准确率影响极小（仅降1.6个百分点），但会大幅削弱小模型的不确定性信号可靠性，小模型尽量避免4bit量化，优先扩容上大模型量化版本

  - 业务如果涉及用户上传低质实拍图（低光、过曝、模糊等），除了置信度拒识逻辑，必须加上游图像质量前置检查，避免极端场景下置信度失效漏错'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
VLM目前大量落地在消费级GPU、边缘设备场景，输入图像常存在压缩、模糊、低光、眩光等真实退化问题，可靠的不确定性信号是模型错误拒识、转人工处理的核心依据。但固定内存预算下，小模型全精度、小模型量化、大模型量化三类可行配置的不确定性信号表现差异未被系统测量，从业者缺乏明确选型依据。
### 方法关键点
- 对照实验设置：选取Qwen2-VL系列三类适配16GB显存的配置做正交对比：2B fp16（小模型全精度）、2B 4bit（小模型量化）、7B 4bit（大模型量化），隔离规模和量化的影响
- 场景覆盖：设计6类真实拍摄退化（JPEG压缩、运动模糊、低光、眩光、旋转、重采样）各3个 severity 等级，匹配端侧真实输入特征
- 信号与指标：同时评估两类置信度信号（模型口头输出的verbalized confidence、生成答案token的平均internal confidence），核心指标采用错误检测AUROC，直接衡量信号用于拒识的可用性
### 关键结果
基于Food101数据集的100样本四选任务共完成5700次预测，核心结论：
1. 规模提升（2B→7B，同4bit精度）：内部置信度AUROC从0.80升至0.98，verbalized confidence仅从0.61升至0.69，仍接近随机水平
2. 4bit量化（同2B参数量）：准确率仅下降1.6个百分点，但内部置信度AUROC从0.95跌至0.80，verbalized confidence解析率从99%暴跌至64%
3. 固定16GB预算下，7B 4bit表现全面最优：准确率0.935、内部AUROC 0.98，均优于2B全精度版本，且其置信度阈值可跨退化场景迁移，不会漏判错误

**最值得记住的一句话**：固定内存预算下优先把资源花在参数量上而非精度上，一定要用生成token的平均概率作为置信度信号，不要相信模型自己输出的置信度数值。
