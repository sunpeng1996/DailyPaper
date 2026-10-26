---
title: 'AVAtt: A Free-Viewing Eye-Tracking Dataset and Benchmark for Visual Attention
  on Paintings'
title_zh: AVAtt：面向绘画视觉注意力的自由观看眼动数据集与基准
authors:
- Mohamed Amine Kerkouri
- Marouane Tliba
- Aladine Chetouani
- Alessandro Bruno
affiliations:
- F-Initiatives, France
- University of Orléans, PRISME Laboratory, France
- IULM University, Milan, Italy
arxiv_id: '2610.30481'
url: https://arxiv.org/abs/2610.30481
pdf_url: https://arxiv.org/pdf/2610.30481
published: '2026-10-21'
collected: '2026-10-26'
category: Other
direction: 视觉注意力 · 绘画眼动数据集与基准
tags:
- Eye-Tracking
- Saliency
- Dataset
- Benchmark
- Scanpath
one_liner: 发布覆盖16种艺术流派的绘画眼动数据集AVAtt，基准测试现有显著性与扫描路径模型性能
practical_value: '- 电商商品主图、Banner视觉优化可复用「人脸优先吸引注意力、局部结构引导眼动」的结论，优化素材排版提升点击率

  - 评估视觉素材吸引力的指标体系，可参考论文排序的44种扫描路径相似度度量，以及基于CNN/ViT的无语言图像编码器指标

  - 艺术品类电商的推荐/搜索场景，可直接复用AVAtt数据集的艺术元数据与用户眼动特征，优化艺术类商品的视觉匹配模型'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有显著性、扫描路径模型几乎全部基于自然照片训练，而绘画由艺术家刻意构图引导视线，纹理、色彩、抽象度与照片差异显著，缺乏对应标注数据集支撑模型优化。
### 方法关键点
构建AVAtt自由观看眼动数据集，覆盖16种艺术流派、5个世纪的283幅绘画，采集152名参与者的4505条扫描路径、121426个注视点；每幅画配套扫描路径时序/眼屏距离、注视图、显著性图、时序显著性视频、艺术元数据；基准测试经典与深度显著性模型，排序44种扫描路径相似度度量，新增基于CNN、ViT、自监督编码器的无语言图像编码器指标族。
### 关键结果数字
人脸被注视概率是预期的5倍，且首次注视发生在500ms以内；现有模型在艺术场景仍有较大性能提升空间；艺术风格显著影响观看者注意力一致性。
