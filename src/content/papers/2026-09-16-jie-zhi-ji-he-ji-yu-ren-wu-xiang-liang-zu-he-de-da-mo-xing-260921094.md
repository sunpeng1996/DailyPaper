---
title: 'Geometry of Values: Task Vector Composition for Ethical Preference Alignment
  in Language Models'
title_zh: 价值几何：基于任务向量组合的大模型伦理偏好对齐
authors:
- Utkarsh Agarwal
- Monojit Choudhury
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2609.21094'
url: https://arxiv.org/abs/2609.21094
pdf_url: https://arxiv.org/pdf/2609.21094
published: '2026-09-16'
collected: '2026-09-21'
category: LLM
direction: 大模型偏好对齐 · 任务向量编辑
tags:
- Task Vector
- Preference Alignment
- LoRA
- DPO
- Multilingual LLM
one_liner: 提出任务向量正交分解方法，无需重训即可切换大模型伦理偏好，保留96%以上微调性能
practical_value: '- 多偏好切换的Agent/内容审核场景，可复用任务向量正交分解思路，将通用指令向量与特定偏好向量解耦，仅通过向量加减切换偏好，无需存储多份微调模型、无需重训，大幅降低部署和调整成本

  - 端侧小模型（1B-3B）做偏好对齐时优先选LoRA SFT/DPO方案，仅需5 epoch训练即可消除位置偏见，准确率可达98%+，训练成本极低

  - 跨语种服务场景不要完全依赖prompt做偏好引导，prompt在低资源语种上准确率最高下降24%，轻量PEFT微调的稳定性远高于prompt steering'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型在内容审核、决策辅助、Agent服务等场景需处理冲突的道德价值判断，但开箱模型存在固有价值偏见与位置偏见，prompt引导跨语种脆性高，切换偏好需反复微调成本高，缺乏模块化的偏好调整方案。
### 方法关键点
- 构建12000条多语种（中英阿西印）伦理困境数据集，覆盖诚实、正义、自主性三类核心价值的两两冲突场景，配套人工标注的OOD黄金测试集。
- 采用LoRA对Llama-3.2 1B/3B做SFT/DPO微调，对齐指定价值偏好。
- 提出Task Vector正交分解方案：将微调得到的任务向量拆分为通用指令向量与特定偏好向量，仅反转偏好向量即可实现偏好方向切换，无需重训。
### 关键结果
- 零样本GPT-5-MINI存在稳定的固有价值偏好，跨语种一致倾向诚实>自主性，prompt引导下低资源语种（印地语）准确率最高下降24%。
- LoRA微调后小模型完全消除位置偏见，合成测试集准确率>98%，人工黄金测试集准确率>90%，SFT与DPO性能接近。
- 任务向量切换偏好可保留3B模型96%以上的全微调性能，1B模型也可保留80%以上性能。
### 核心结论
大模型的特定偏好信息可与通用指令能力解耦，通过权重空间的线性运算即可实现无训练的偏好切换，大幅降低多偏好场景的部署与调整成本。
