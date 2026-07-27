---
title: 'Small Vision-Language Models Know When They Are Wrong But Cannot Say So: A
  Two-Model Study of Stated versus Internal Confidence Under Realistic Image Degradation'
title_zh: 小参数视觉语言模型口头与内部置信度在图像退化场景的对比研究
authors:
- M M Asif Ferdous
affiliations:
- Independent Researcher
arxiv_id: '2607.22034'
url: https://arxiv.org/abs/2607.22034
pdf_url: https://arxiv.org/pdf/2607.22034
published: '2026-07-24'
collected: '2026-07-27'
category: Eval
direction: 多模态模型评估 · 置信度校准
tags:
- VLM
- Confidence Calibration
- Uncertainty Estimation
- Edge Deployment
- Model Evaluation
one_liner: 对比小VLM的两类置信度信号，验证内部token概率是更可靠的错误检测与系统降级依据
practical_value: '- 部署端侧小VLM做商品图理解、AR导购等业务时，不要用模型口头输出的置信度做降级判断，优先取生成回答的平均token概率作为置信度信号，错误检测AUROC可提升至少20个点

  - 低光照/重度压缩的劣质商品图场景，两类置信度信号都失效，建议前置图像质量检测模块，低质量图直接走降级流程（比如转人工/召回相似商品），避免错误输出

  - 小VLM做端侧内容审核、商品属性识别时，可直接复用内部token概率阈值做错误兜底，不需要额外训练置信度校准分支，降低部署成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
端侧部署的小参数VLM常面临压缩、抖动、低光照等图像退化场景，需要可靠的不确定性信号判断何时系统降级，现有口头置信度的可靠性未被验证。

### 方法关键点
选取Qwen2-VL-2B-Instruct、SmolVLM-Instruct两款开源小VLM，覆盖6类现实图像退化、3个严重程度，对比模型口头输出的置信度、生成回答的平均token概率两类信号的错误检测能力，共测试3800条预测。

### 关键结果数字
Qwen2-VL口头置信度错误检测AUROC仅0.39~0.75（均值约0.5，接近随机），内部token概率AUROC达0.92~0.99；SmolVLM口头置信度大多无法解析，内部概率AUROC为0.54~0.92；严重低光照场景下两类信号均失效，模型准确率分别降至0.22、0.42，错误检测能力接近随机。
