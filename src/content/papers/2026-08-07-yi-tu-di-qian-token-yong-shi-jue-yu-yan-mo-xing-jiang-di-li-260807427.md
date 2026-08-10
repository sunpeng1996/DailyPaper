---
title: 'A Picture is Worth a Thousand Tokens: How Vision Language Models Cut AI Energy
  Costs While Improving Accuracy'
title_zh: 《一图抵千Token：用视觉语言模型降低AI推理能耗同时提升精度》
authors:
- Bhavika Jalli
- Nikhil Korati Prasanna
- Jayanta Choudhury
affiliations:
- Ericsson
arxiv_id: '2608.07427'
url: https://arxiv.org/abs/2608.07427
pdf_url: https://arxiv.org/pdf/2608.07427
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态大模型 · 推理能效优化
tags:
- VLM
- Inference Efficiency
- Time Series
- Energy Saving
- Anomaly Detection
one_liner: 将时序数据转2D图输入VLM，实现3.6-10.4倍Token压缩，同时降1.8-2.5倍推理能耗提精度
practical_value: '- 处理用户行为时序、商品销量波动、广告投放效果异常检测等业务时，可将多维时序转成无刻度堆叠子图喂给VLM，既压缩Token量降低推理成本，还能提升识别精度，避免长文本溢出上下文窗口

  - 推理成本敏感的大流量业务（如实时指标监控、批量用户标签生成），可将结构化数值序列转成图像模态输入，搭配75DPI低分辨率+JPEG压缩trick，无需重训模型就能再降24%推理能耗，精度损失<2%

  - 边缘端部署大模型做时序类任务时，优先选固定视觉Token预算的VLM架构（如Llama-3.2-Vision系列），可获得确定性能耗指标，方便容量规划，避免文本模式下Token超限导致的OOM问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM推理能耗占AI全生命周期能耗的90%以上，且与输入Token数线性正相关。处理数值时序数据时，少量多维度KPI窗口就会膨胀至数万Token，不仅能耗极高，还容易超过生产级LLM的上下文窗口上限，边缘端部署甚至会触发OOM，现有方案未量化对比LLM与VLM处理时序的端到端能效差。

### 方法关键点
- 单/多变量时序数据渲染为无刻度、无标签、无网格的2D图，多变量采用共享时间轴的垂直堆叠子图格式，保留变量间时间对齐关系
- 选择Llama-3.2-90B-Vision、Qwen2.5-VL-72B、Pixtral-12B三类主流VLM架构做跨架构验证，通过Zeus框架读取GPU硬件能耗计数器实现精准能耗测量
- 额外验证图像分辨率压缩、格式压缩对能效与精度的影响

### 关键结果
基于公开AWSCloudwatch时序数据集、真实电信209个4G/5G小区KPI数据集测试，对比文本LLM、ARIMA、LSTM基线：输入Token量降低3.6~10.4倍，推理能耗降低1.8~2.5倍，电信场景下微调Llama-3.2-90B-Vision精度比文本版高220.7%，比传统时序基线高144%；Pixtral-12B在公开数据集上J/F1能效提升20.6倍，24维KPI下文本输入超过128K上下文窗口，VLM模式仍在标准限制内；75DPI低分辨率压缩可再降24%能耗且精度无损失。

**最值得记住的结论**：对于数值时序类任务，将数据从文本模态切换到图像模态喂给VLM，是同时降本、提效、扩大上下文承载量的结构性优化方案。
