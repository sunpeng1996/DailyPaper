---
title: 'RankGround: Efficient High-Resolution GUI Grounding via Lightweight Reranker-Guided
  Crop Selection'
title_zh: RankGround：轻量级重排序引导裁剪的高效高分辨率GUI定位方法
authors:
- Liyang Fan
- Xinping Bi
- Yitai Li
- Shuaimin Li
- Hui Li
- Min Yang
affiliations:
- 深圳大学
- 中国科学院深圳先进技术研究院
- 厦门大学
- 深圳高等技术研究院
arxiv_id: '2609.18690'
url: https://arxiv.org/abs/2609.18690
pdf_url: https://arxiv.org/pdf/2609.18690
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: 多模态Agent · GUI定位性能优化
tags:
- GUI Grounding
- Multimodal Reranker
- VLM
- LoRA
- Multimodal Agent
one_liner: 轻量多模态重排序引导裁剪选择，实现单VLM调用的高效高分辨率GUI定位
practical_value: '- 开发电商多模态Agent（如商家后台自动操作、自动选品工具）的GUI交互模块时，可复用「轻量reranker选裁剪区+单VLM预测坐标」架构，比多VLM调用方案提速1.4x，精度提升5.5%

  - 多模态重排序器训练可复用「严格包含标注+边界感知增强+pointwise到listwise两阶段课程」方案，仅用LoRA微调即可大幅提升区域选择准确率，训练成本极低

  - 高分辨率多模态任务中，可复用50%重叠的分块裁剪策略，能以99.75%概率保证目标落在至少一个裁剪块内，避免不可恢复的识别错误

  - 高分辨率下小目标识别场景不要盲目堆叠大模型调用，优先用轻量预训练模型做前置筛选，性价比更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
高分辨率GUI界面元素密度大、尺寸小，现有GUI定位方案存在精度与效率的核心矛盾：直接全图VLM推理会丢失小目标细节，多裁剪重复VLM调用方案延迟高、部署成本高，无法满足实时多模态Agent的交互需求。
### 方法关键点
- 架构：两阶段解耦区域选择与坐标预测，先用50%重叠分块生成候选裁剪集，轻量GroundRanker选最优裁剪后仅调用1次GUI专用VLM做坐标预测
- 数据：从现有定位数据集自动生成裁剪级标注，以严格完全包含规则划分正负样本，新增边界感知正样本增强消除位置偏差
- 训练：两阶段课程学习，先pointwise二元交叉熵学习基础包含判断，再listwise损失区分相似候选块，仅对重排序器的Q/V投影层做LoRA微调
### 关键结果
在ScreenSpot-Pro高分辨率GUI基准上，跨所有骨干模型与2B/8B尺度，平均定位精度比次优方法高5.5%，推理速度快1.4倍；跨5个不同GUI基准均优于ZoomIn等多VLM调用方案，跨域UI-Vision数据集上精度比直接全图推理高30.12pct。
### 核心洞察
高分辨率多模态定位的核心瓶颈是区域选择而非坐标预测，轻量前置筛选远比重复调用大VLM性价比更高。
