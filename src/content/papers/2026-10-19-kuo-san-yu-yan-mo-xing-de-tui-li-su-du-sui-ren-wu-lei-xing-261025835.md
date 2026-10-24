---
title: Diffusion Language Models Change Speed Across Tasks and Languages
title_zh: 扩散语言模型的推理速度随任务类型与语言差异显著变化
authors:
- Mohsen Fayyaz
- Ali Modarressi
- Daniel Israel
- Lucas Bandarkar
- Nanyun Peng
affiliations:
- University of California, Los Angeles
- CIS, LMU Munich
- Munich Center for Machine Learning
arxiv_id: '2610.25835'
url: https://arxiv.org/abs/2610.25835
pdf_url: https://arxiv.org/pdf/2610.25835
published: '2026-10-19'
collected: '2026-10-24'
category: LLM
direction: 扩散大语言模型 · 推理效率优化
tags:
- DiffusionLLM
- InferenceEfficiency
- DecodingSpeed
- Multilingual
- AnswerSelection
one_liner: 揭示扩散LLM推理成本的多维度影响因素，提出无额外开销的解码速度加权答案选择方法
practical_value: '- 业务中可优先将客服回复、商品文案改写等输入依赖度高的任务适配扩散LLM，这类任务推理成本比开放式生成低3倍以上，大幅降本

  - 跨境电商多语言内容生成场景需提前调度资源：低资源语言存在双重成本 penalty，token数更多且每token需要的forward pass也更多

  - 做推理类任务（如营销效果归因、选品决策）时，可用解码速度作为无额外开销的置信度信号，替代昂贵的多数投票，相同采样数下准确率可提升2-4个点

  - 涉及思维链的Agent任务中，针对复制思维链内容的最终回答阶段可简化解码策略，进一步降低推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散LLM支持单次forward pass生成多个token，推理速度远高于自回归LLM，但相同长度输出的推理成本波动极大，业界缺乏对成本影响因素的系统性研究，也没有把成本特性落地的实用优化方法。

### 方法关键点
- 测试两款主流扩散LLM：26B MoE结构的DiffusionGemma、8B dense结构的DreamReasoner，均采用动态step自适应解码逻辑
- 定义核心成本指标：每生成100个输出token所需的forward pass数，自回归LLM的该指标固定为100
- 覆盖10类任务分为三组：重输入复制的重现类、依赖上文生成的链式类、低约束的开放式类，补充25种语言的翻译任务做多语言成本分析

### 关键结果数字
- 任务维度：DiffusionGemma的重现类任务平均成本为4.0，链式类5.8，开放式9.8，故事生成成本是语法校正的3.1倍；成本与输出新信息量（输入相似度+任务内词频surprisal的乘积）相关性最高，达0.76
- 推理类任务：错误答案的成本比正确答案高1.2次/100token，用解码速度加权投票比多数投票在2采样时准确率高4.2个点，5采样时高2.3个点，无额外计算开销
- 多语言维度：token切分越细的语言，每token成本越高，和token生育率的相关性达0.65，低资源语言存在双重成本 penalty

最值得记住的结论：扩散LLM的推理效率高度依赖输出的确定性，解码付出的计算量本身就是模型置信度的免费信号。
