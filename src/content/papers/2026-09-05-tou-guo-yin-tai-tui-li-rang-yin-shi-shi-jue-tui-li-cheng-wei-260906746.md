---
title: Reason Through the Latent! Making Latent Visual Reasoning Necessary
title_zh: 透过隐态推理：让隐式视觉推理成为模型必选的预测依赖路径
authors:
- Suhyeong Park
- Junha Jung
- Jaewoo Kang
affiliations:
- Korea University
- AIGEN Sciences
arxiv_id: '2609.06746'
url: https://arxiv.org/abs/2609.06746
pdf_url: https://arxiv.org/pdf/2609.06746
published: '2026-09-05'
collected: '2026-09-10'
category: Reasoning
direction: 多模态隐式视觉推理能力优化
tags:
- Latent Reasoning
- Multimodal Reasoning
- KV Cache
- Causal Intervention
- Visual Reasoning
one_liner: 提出因果视觉循环推理框架CVRR，强制多模态模型依赖隐状态路径完成视觉推理且保留预训练能力
practical_value: '- 多模态商品理解/搜图场景可复用CVRR的强制依赖隐状态思路，避免模型偷跑依赖文本旁路，提升视觉特征的实际作用

  - 推理侧KV cache截断技巧可直接复用，强制后续解码仅依赖指定隐状态，降低无关信息干扰，适合可控多模态生成场景

  - 因果干预验证隐状态实际贡献的方法，可用于多模态推荐模型消融实验，快速定位特征是否被模型真实使用'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有隐式视觉推理无法保证模型真实依赖隐状态计算，仍可能绕过隐层直接使用原始图像条件路径输出结果，无法验证隐推理的实际贡献。
### 方法关键点
1. 提出CVRR框架，基于预训练多模态模型，以图像与问题融合后的问题隐状态初始化循环计算，重复读取固定视觉证据更新隐状态。
2. 解码前移除所有视觉状态和原始多模态KV cache，强制仅最终循环隐状态承载图像相关信息输入解码环节，确保隐推理是唯一的图像依赖路径。
### 关键结果
在V*、MMVP、BLINK、MME-RealWorld-Lite 4个基准上，CVRR在严格约束下性能无明显下降；同条件下其他隐推理方法即使重训也无法达到相当的视觉能力；因果干预验证问题固定时预测对循环内容敏感，视觉证据可因果性修正循环轨迹。
