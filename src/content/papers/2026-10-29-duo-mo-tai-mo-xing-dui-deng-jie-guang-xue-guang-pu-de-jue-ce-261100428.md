---
title: Do Multimodal Models Decide Consistently on Equivalent Optical Spectra?
title_zh: 多模态模型对等价光学光谱的决策是否具备一致性？
authors:
- Ziyuan Wang
- Genliang Zhu
- Xiaobo Chen
affiliations:
- Independent Researcher
- Georgia Institute of Technology
- University of Massachusetts Amherst
arxiv_id: '2611.00428'
url: https://arxiv.org/abs/2611.00428
pdf_url: https://arxiv.org/pdf/2611.00428
published: '2026-10-29'
collected: '2026-11-14'
category: Eval
direction: 多模态模型决策一致性评估
tags:
- Multimodal LLM
- Model Evaluation
- Representation Invariance
- LoRA Fine-tuning
- Abstention Mechanism
one_liner: 测试多模态模型在等价光谱不同表征下的决策一致性，揭示准确率波动与训练捷径问题
practical_value: '- 做LLM/Agent业务评测时，不能仅看平均准确率，需补充等价输入的一致性测试，如同个用户意图换多种表达方式、同个商品换多种参数表示格式，避免实际场景的决策波动

  - 给业务LLM做LoRA微调时，要警惕模型学到数据捷径，比如只要看到截断输入就拒答，可通过加入带截断的可回答样本训练高效规避该问题

  - 涉及多模态输入（如商品参数表、实拍图、规格示意图等等价信息）的导购Agent/商品理解模块，要预先测试不同输入格式下的输出一致性，减少bad case'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
相同物理含义的光学光谱可呈现为不同单位的数值表、不同坐标轴的图像等多模态格式，多模态模型决策结果应与表征格式无关，信息不足时应主动拒答，但现有模型的相关能力未被系统性验证。
### 方法关键点
基于硅超构表面、金纳米颗粒的实测光学光谱，生成4种单位的数值表、2种坐标轴的图像、截断的部分光谱作为输入，测试d3-nano、GPT-6 Luna、Qwen3.5-2B等模型的表征不变性与拒答能力。
### 关键结果数字
仅改变输入表征即可让单模型准确率波动最高41个百分点；同证据下提问单位换为光子能量可让部分模型效果提升16-50个百分点、部分下降最高25个百分点；未适配模型在关键信息缺失时极少主动拒答；直接LoRA微调会让模型学到「见截断就拒答」的捷径，加入截断可回答样本训练可完全规避该问题，内外截断场景的拒答准确率差达90-100个百分点。
