---
title: 'DR Pixel: Page-Native Deep Research with Vision-Language Models'
title_zh: DR Pixel：基于视觉语言模型的页面原生深度研究Agent
authors:
- Tiansheng Hu
- Yichuan Wang
- James V. Talwar
- Nicholas Tomlin
- Chen Zhao
- Sewon Min
affiliations:
- NYU Shanghai
- UC Berkeley
- Rational Dynamics
- Toyota Technological Institute at Chicago
- New York University
arxiv_id: '2611.03097'
url: https://arxiv.org/abs/2611.03097
pdf_url: https://arxiv.org/pdf/2611.03097
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: 多模态Agent · 深度研究RAG优化
tags:
- VLM
- Deep Research Agent
- Multimodal RAG
- Counterfactual Credit Assignment
- OCR-free
one_liner: 首个开源页面原生多模态深度研究Agent，无需OCR，反事实训练后性能赶超GPT-5.4
practical_value: '- 电商/广告场景下的商品详情页、活动规则页、资质文档等多模态内容检索，可直接跳过OCR，用页面渲染图像做VLM检索+推理，避免结构化信息丢失，提升多模态RAG准确率

  - 多轮Agent的SFT训练可复用反事实信用重加权方法，给轨迹中每个动作/推理步骤打分，过滤冗余无效步骤，减少不必要的工具调用，提升Agent执行效率

  - 处理布局复杂的多模态文档（如商家财报、平台规则、营销物料）时，可直接采用页面原生Pipeline，省掉OCR、结构化解析的繁琐开发维护成本，适配任意排版的文档

  - DRPixelBench可直接用于评估自家多模态RAG/Agent的多轮检索+复杂推理能力，填补现有多模态评测集缺乏长推理链的空白'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有深度研究（DR）Agent依赖OCR将文档转换为纯文本处理，会丢失图表、公式、排版等关键视觉信息，OCR误差还会向下游传播；且分离的文本、图像检索割裂了同页面内容的关联，导致多模态复杂推理任务性能低、工具调用成本高。
### 方法关键点
- 架构层面完全摒弃OCR Pipeline：将所有文档逐页渲染为图像，作为唯一的检索和推理单元，用VLM embedding模型做页面检索，VLM Agent直接基于检索到的图像迭代执行搜索、推理、回答，全程不做文本转换。
- 训练阶段提出**反事实信用重加权**：对Teacher模型生成的轨迹中每个推理、搜索步骤，通过移除该步骤后答案质量的变化计算贡献度，仅给高贡献步骤分配训练权重，过滤冗余或错误的无效步骤。
- 构建DRPixelBench评测集：包含500个非模板化、答案可验证的科学文献问题，覆盖文本、表格、图像、公式多模态推理，需多轮检索才能得到正确答案。
### 关键结果
在1.06M页科学文献语料上测试：
1. 无训练版本跨GPT-5.4、Gemini-3.5-Flash、Qwen3.6-27B三个模型，准确率比OCR基线高5.1~8.4个点，工具调用量少20%~30%。
2. 用反事实方法训练Qwen3.6-27B后，准确率较无训练版本提升12个点，在DRPixelBench上准确率超过GPT-5.4；在OOD数据集ViDoRe-V3上，与直接给定金页的Oracle性能仅差1.8个点。
### 核心结论
传统OCR-then-retrieve的Pipeline不仅不必要，甚至是次优的，直接基于页面图像做检索和推理可让复杂深度研究任务同时提升效率和效果。
