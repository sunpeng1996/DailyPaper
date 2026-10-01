---
title: 'FocusVTC: Efficient and High-Performance Visual Text Compression with Adaptive
  Resolution'
title_zh: FocusVTC：基于自适应分辨率的高效高性能视觉文本压缩
authors:
- FangZhi Zhong
- Xuerui Qiu
- Yuqi Pan
- Ya Liu
- Shaowei Gu
- Bo Xu
- Guoqi Li
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- School of Artificial Intelligence, University of Chinese Academy of Sciences
- Shanghai Jiao Tong University
- Zhongguancun Academy
arxiv_id: '2609.36651'
url: https://arxiv.org/abs/2609.36651
pdf_url: https://arxiv.org/pdf/2609.36651
published: '2026-09-28'
collected: '2026-10-01'
category: Multimodal
direction: 多模态LLM · 长上下文压缩
tags:
- Visual Text Compression
- Long Context LLM
- Adaptive Resolution
- GRPO
- Multimodal LLM
one_liner: 提出自适应分辨率视觉文本压缩框架，打破压缩性能权衡，保留通用多模态能力
practical_value: '- 长上下文RAG/Agent场景可复用「低分辨率全局检索+高分辨率局部增强」的思路，处理电商商品详情、用户评论、合同等长文本时，大幅降低token成本同时保证信息召回准确率

  - 工具调用型Agent训练可借鉴「SFT教定位+GRPO调调用策略」的两阶段范式，结合业务场景构造关联推理路径与证据位置的CoT数据，大幅降低无效工具调用率

  - 多模态OCR/文档理解任务可复用渲染参数优化trick：提前对字体、字号、DPI做ablation，选择兼顾识别准确率和视觉token成本的最优配置，文中DejaVu
  Sans 9pt比Verdana在长文本任务上高1.47分'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM推理的计算、KV缓存成本随上下文长度线性增长，现有视觉文本压缩（VTC）方案将文本渲染为图像用VLM编码为短视觉token序列降低输入长度，但固定分辨率渲染存在固有权衡：低DPI压缩率高但易丢失细节导致准确率下降，高DPI识别准但token浪费在无关内容，无法兼顾压缩效率与推理性能。
### 方法关键点
- 自适应推理框架：先输入低DPI全局页面做全局推理，定位到关键证据区域后调用工具返回该区域的高DPI渲染结果，融合后继续推理，无需全页高DPI编码
- 数据构造：构建29.4K高质量REL-CoT数据集，每条样本关联推理路径、答案与对应证据的页码、归一化bounding box，覆盖单/多跳QA、数值推理等场景
- 两阶段训练：第一阶段用多分辨率REL-SFT训练模型跨7种DPI定位证据，无需持续预训练；第二阶段用GRPO强化学习优化增强时机、区域选择、结果融合与停止策略，奖励结合答案准确率、格式合规性与工具调用效率
### 关键结果
在72DPI设置下：RULER v1上2.9倍压缩率时得分87.4，远超同压缩率下Glyph的57.5；LongBench得分56.40，超过文本输入的Qwen3.5-9B基线的55.86；MRCR macro平均提升13.91分，端到端延迟比文本输入快2.79倍；通用多模态能力无损失，MMU从65.12提升至66.73，MME从2424.02提升至2457.62。
### 核心结论
根据推理需求动态分配视觉计算资源，可在高压缩率下同时实现优异的长上下文推理性能与通用多模态能力。
