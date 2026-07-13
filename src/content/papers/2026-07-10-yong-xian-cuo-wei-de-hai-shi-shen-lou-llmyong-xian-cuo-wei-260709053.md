---
title: 'An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust
  Phenomenon?'
title_zh: 涌现错位的海市蜃楼：LLM涌现错位与重对齐现象的稳健性验证
authors:
- Abhinav Rao
- Liancheng Gong
- Bin Hu
- Atharva Naik
affiliations:
- University of Maryland
- Carnegie Mellon University
arxiv_id: '2607.09053'
url: https://arxiv.org/abs/2607.09053
pdf_url: https://arxiv.org/pdf/2607.09053
published: '2026-07-10'
collected: '2026-07-13'
category: LLM
direction: 大语言模型 · 对齐与涌现错位鲁棒性研究
tags:
- Emergent Misalignment
- LLM Alignment
- LoRA
- Fine-tuning
- Evaluation
one_liner: 验证LLM涌现错位与重对齐是依赖数据集表层特征的脆弱现象，现有机制信号无稳定相关性
practical_value: '- 垂直领域LLM微调（如电商客服、营销文案生成）时，需严格控制训练集的回答长度、格式等表层特征，避免将特征导致的效果波动误判为模型真实能力变化

  - 基于LoRA做业务模型迭代时，不要过度依赖LoRA参数余弦相似度、梯度突变等内部信号判定模型效果跃迁，此类信号与实际业务表现无稳定相关性

  - 电商/广告场景的LLM安全对齐无需过度担心窄领域微调导致的全局错位风险，现有EM现象非常脆弱，仅需少量特征匹配的对齐样本即可完成修正'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
此前研究报道LLM在窄领域错位数据集微调时会突发全局涌现错位（EM），且仅需少量样本即可完成重对齐，但对齐评估缺乏连续平滑度量，现有结论是否受数据集表层特征干扰尚未验证，循环对齐-错位过程中的模型可塑性变化也不明确。
### 方法关键点
- 基于Qwen2.5-14B-Instruct模型，分别采用rank-1单LoRA、rank-32全模块LoRA两种参数高效微调配置
- 设计两类循环微调流程：错位→对齐→错位、对齐→错位→对齐，使用配对的风险金融建议数据集（每道问题对应对齐/错位两份回答）
- 全程跟踪LoRA参数余弦相似度、梯度范数等机制信号，采用GPT-4o-mini做对齐评分（得分<30且连贯性>50判定为错位）
### 关键结果
- 未控制回答长度时，重对齐仅需40个样本即可让错位率下降90%以上，且后续再次错位尝试失效；控制回答长度匹配后，循环错位/重对齐均可稳定复现
- 此前报道的LoRA空间相变、梯度尖峰等机制信号，与实际错位行为无稳定相关性，LoRA参数漂移全程呈振荡特征
- 对齐训练阶段的梯度范数比错位训练阶段平均低30%，说明预训练对齐模型更易适配对齐数据
### 核心结论
现有涌现错位现象的鲁棒性被严重高估，多数观测到的对齐/错位行为变化本质是数据集表层特征导致的评估假象
