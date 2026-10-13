---
title: 'S-Space: Exploring Spatial Workspace in Multimodal Language Models'
title_zh: S-Space：多模态大语言模型内部空间工作区机制探究
authors:
- Zhiyuan Shi
- Xiang Li
- Xingzhuo Guo
- Shangchen Miao
- Weiliang Chen
- Qiyu Dai
- Jinshan Ren
- Jiangran Lyu
- Fangfu Liu
- Mingsheng Long
affiliations:
- MirroS
- Mirros Lab
arxiv_id: '2610.13527'
url: https://arxiv.org/abs/2610.13527
pdf_url: https://arxiv.org/pdf/2610.13527
published: '2026-10-09'
collected: '2026-10-13'
category: Reasoning
direction: 多模态大模型 · 空间推理可解释性
tags:
- MLLM
- Spatial Reasoning
- Interpretability
- Representation Subspace
- Model Diagnosis
one_liner: 发现多模态大模型内部固有线性子空间S-Space，可解释空间推理机制并定位性能瓶颈
practical_value: '- 做多模态商品理解/AR虚拟陈列/试穿场景的Agent，可借鉴S-Space读取方法抽取图像中商品的空间坐标，无需额外标注训练空间属性识别模型

  - 空间推理类Agent（如线下导购路径规划、仓储拣货路径生成）可复用S-Space的感知-计算分解框架，定位空间变换环节的性能瓶颈做定向优化

  - MLLM落地空间相关任务时，可通过干预S-Space表征的方式定向修正空间判断结果，同时不影响非空间类响应的准确性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
多模态大模型（MLLMs）已具备可观的空间推理能力，但内部支撑机制不明确，难以定位推理失败根因，限制了空间类任务的性能优化。
### 方法关键点
通过对空间答案得分关于object token激活的梯度微分，识别到MLLM内部固有线性表征子空间S-Space，其内置水平、垂直、距离三个坐标轴，可编码物体连续坐标；结合因果干预、感知-计算分解等方法验证S-Space的功能边界。
### 关键结果
1. S-Space为MLLM固有属性，不受特定数据或Prompt诱导，非空间问题场景下仍可稳定读取；
2. 因果干预修改S-Space表征时，空间判断结果可被定向修改，同时非空间类响应基本不受影响；
3. 明确MLLM空间推理核心瓶颈：空间表征构建能力达标，但视角变换所需的空间变换环节可靠性不足。
