---
title: 'ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters'
title_zh: ScaleVLA：将视觉-语言-动作模型扩展至5520亿参数规模
authors:
- Ruixi Yu
- Dairu Liu
- Xuchuan Chen
- Zekun Qi
- Zekai Li
- Zhuo Cao
- Luyang Niu
- Yingsheng Zhang
- Sikai Liang
- Ke Fan
affiliations:
- Tsinghua University
- Peking University
- Shanghai Jiao Tong University
- Galbot
arxiv_id: '2611.21607'
url: https://arxiv.org/abs/2611.21607
pdf_url: https://arxiv.org/pdf/2611.21607
published: '2026-11-15'
collected: '2026-11-17'
category: Multimodal
direction: 多模态大模型 · 大参数量VLA策略构建
tags:
- VLA
- Multimodal-LLM
- Large-Scale-Model
- DiT
- Robot-Policy
one_liner: 将552B参数大VLM对接可训练动作DiT，构建性能远超小模型的低延迟机器人VLA策略
practical_value: '- 架构可复用：多模态Agent/生成式推荐场景可采用「冻住大参数量多模态底座 + 仅训练下游轻量任务头」范式，兼顾性能与训练成本

  - 结论可参考：少样本业务场景（如新类目商品理解、小众用户偏好建模）优先升级大参数量底座，比给小底座喂更多数据性价比更高

  - 工程优化思路：大模型在线推理可借鉴Flash系列大模型的低延迟优化方案，552B规模也可做到200ms级延迟满足实时要求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA策略普遍采用小参数量VLM骨干，无法充分释放大参数量VLM预训练获得的通用视觉感知、空间推理、知识理解能力，机器人任务性能存在明显瓶颈。
### 方法关键点
ScaleVLA架构采用冻住552B参数DeepSeek-V4.1-Flash多模态骨干，仅对接训练轻量动作DiT头的设计，在统一训练设置下系统对比2B到552B不同参数量VLM的VLA任务表现。
### 关键结果
- 样本效率：仅10条演示训练的552B模型准确率87.8%，超过50条演示训练的2B模型的85.6%
- 泛化能力：LIBERO-PRO任务成功率达45.1%，远超小模型最高的31.3%
- 精确操作：真实场景充电器插拔成功率从4/10提升至9/10
- 推理延迟：单动作块中位数延迟仅216ms，满足实时交互要求
