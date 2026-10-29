---
title: 'Watermark Basins: Black-Box Detection of Distilled LLMs'
title_zh: 水印盆地：蒸馏大语言模型的黑盒检测方法
authors:
- Hongyan Chang
- Hady Elsahar
- Tom Sander
- Pierre Fernandez
- Saeed Mahloujifar
- Sylvestre-Alvise Rebuffi
- Tomáš Souček
- Tuan Tran
- Valeriu Lacatusu
- Surya Parimi
affiliations:
- FAIR, Meta Superintelligence Labs
arxiv_id: '2610.37266'
url: https://arxiv.org/abs/2610.37266
pdf_url: https://arxiv.org/pdf/2610.37266
published: '2026-10-27'
collected: '2026-10-29'
category: LLM
direction: 大语言模型 · 蒸馏水印检测
tags:
- LLM-Watermark
- Black-Box-Detection
- Model-Distillation
- Parameter-Space-Signal
- LLM-Security
one_liner: 发现参数空间正交的水印盆地信号，提出蒸馏LLM黑盒检测方案WM-Basin，显著超越SOTA基线
practical_value: '- 做自家LLM生成内容（电商文案、推荐理由、Agent回复）的版权保护时，可叠加基于参数空间的水印盆地信号，相比传统token级水印更难被蒸馏抹去，抗量化、剪枝等后处理，适合多端部署小模型的版权溯源

  - 调用第三方LLM做下游推荐/Agent业务时，可参考WM-Basin的黑盒检测思路，无需获取模型权重即可验证第三方模型是否盗用了自家训练的蒸馏模型，保障业务知识产权

  - 做生成式推荐的Semantic ID、个性化文案生成时，可借鉴正交子空间投影思路，将业务专属信号嵌入模型参数的正交子空间，不影响主任务性能的同时实现版权溯源'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
现有API蒸馏LLM的黑盒水印检测依赖token级统计信号，低温度采样时信号易丢失，无法抵抗蒸馏后量化、剪枝等后处理，检测准确率极低。
## 方法关键点
1. 发现水印盆地效应：带水印的教师输出蒸馏时，会在学生模型参数空间嵌入与任务微调子空间正交、密钥唯一的几何信号，不会被任务微调覆盖；
2. 提出WM-Basin黑盒检测器：无需可疑模型权重/logits，仅通过API获取生成文本，用干净探针模型映射为梯度表征，投影剔除普通任务微调方向后，检验残差梯度是否对齐对应密钥的水印盆地即可完成检测。
## 关键结果
在0.1%严格假阳率下，n-gram=1时检测率达79%，n-gram=3时达45%，较现有SOTA token级基线（29%、1.3%）提升数倍，信号可耐受蒸馏后的量化、剪枝、强化学习后训练操作。
